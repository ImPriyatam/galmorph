import pandas as pd
import matplotlib.pyplot as plt
import os
from typing import Optional, Dict, Any, List


class GalMorph:
    """
    A class for analyzing and visualizing galaxy morphology data from numerical simulations.

    Attributes:
        data (pd.DataFrame): DataFrame containing galaxy morphology data loaded from a pickle file.
    """

    def __init__(self, file_path: str):
        """
        Initializes the GalMorph object by loading data from a pickle file.

        Parameters:
            file_path (str): Path to the pickle file containing galaxy morphology data.

        Raises:
            FileNotFoundError: If the pickle file does not exist.
            pd.errors.EmptyDataError: If the pickle file is empty or invalid.
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File '{file_path}' does not exist.")
        try:
            self.data = pd.read_pickle(file_path)
        except Exception as e:
            raise pd.errors.EmptyDataError(f"Could not load pickle file '{file_path}': {e}")

        self._validate_required_columns({"Snapshot", "P_Spheroid", "P_Disk", "P_Irr", "SubhaloID"})

        # Precompute galaxy types for efficiency
        self.data["Galaxy_type"] = self.data.apply(self._assign_galaxy_type, axis=1)

    def _validate_required_columns(self, required_cols: set):
        """
        Checks if required columns are present in self.data.

        Parameters:
            required_cols (set): Set of required column names.

        Raises:
            ValueError: If any required columns are missing.
        """
        missing_cols = required_cols - set(self.data.columns)
        if missing_cols:
            raise ValueError(f"Missing columns in data: {missing_cols}")

    def _assign_galaxy_type(
        self,
        row: pd.Series,
        thresholds: Optional[Dict[str, float]] = None
    ) -> str:
        """
        Assigns a galaxy type based on the highest value among three input columns.

        Parameters:
            row (pd.Series): A row from a DataFrame, containing columns "P_Spheroid", "P_Disk", & "P_Irr"
            thresholds (dict, optional): Dictionary of critical values.

        Returns:
            str: 'elliptical', 'spiral', 'irregular', or 'unknown' depending on which value is highest.
        """
        if thresholds is None:
            thresholds = {'elliptical': 0.7, 'spiral': 0.6, 'irregular': 0.5}
        try:
            values = {
                'elliptical': row["P_Spheroid"],
                'spiral': row["P_Disk"],
                'irregular': row["P_Irr"]
            }
        except KeyError as e:
            raise KeyError(f"Missing expected column in row: {e}")
        max_type = max(values, key=values.get)
        max_value = values[max_type]
        if max_value >= thresholds[max_type]:
            return max_type
        else:
            return 'unknown'

    def galaxy_count(self, file_name: str = "galaxy_count.png", show: bool = False) -> plt.Figure:
        """
        Plots the number of galaxies for each snapshot and saves the plot as an image.

        Parameters:
            file_name (str): Name of the output image file for the plot. Default is "galaxy_count.png".
            show (bool): Whether to display the plot. Default is False.

        Returns:
            plt.Figure: The matplotlib Figure object.
        """
        snapshots = self.data["Snapshot"].drop_duplicates().sort_values()
        galaxies_count = [self.data[self.data["Snapshot"] == val].shape[0] for val in snapshots]

        fig, ax = plt.subplots(figsize=(6, 5))
        ax.plot(snapshots, galaxies_count, ls="-.")
        ax.scatter(snapshots, galaxies_count, marker="o", color="red")
        ax.minorticks_on()
        ax.set_xlabel("Snapshot")
        ax.set_ylabel("Galaxy Count")
        fig.tight_layout()
        try:
            fig.savefig(file_name, dpi=130)
        except Exception as e:
            print(f"Error saving plot to '{file_name}': {e}")
        if show:
            plt.show()
        plt.close(fig)
        return fig

    def galaxy_type_snap(
        self,
        snapshot_num: int = 25,
        output_fname: str = "GalCount.png",
        show: bool = False
    ) -> plt.Figure:
        """
        Plots a bar chart of galaxy type counts for a specific snapshot and saves the plot as an image.

        Parameters:
            snapshot_num (int): The snapshot number to analyze. Default is 25.
            output_fname (str): Name of the output image file for the plot. Default is "bar.png".
            show (bool): Whether to display the plot. Default is False.

        Returns:
            plt.Figure: The matplotlib Figure object.

        Raises:
            ValueError: If the snapshot is not found in the data.
        """
        available_snapshots = sorted([int(s) for s in self.data["Snapshot"].unique()])
        if snapshot_num not in available_snapshots:
            raise ValueError(
                f"Snapshot {snapshot_num} not found in data. "
                f"Available snapshots are: {available_snapshots}"
            )

        snapshot_galaxy = self.data[self.data["Snapshot"] == snapshot_num]
        if snapshot_galaxy.empty:
            raise ValueError(f"No data found for snapshot {snapshot_num}.")

        galaxy_type_counts = snapshot_galaxy["Galaxy_type"].value_counts().to_dict()
        galaxy_type_counts = dict(sorted(galaxy_type_counts.items()))


        from matplotlib import colormaps 

        # Get the tab10 colormap
        color_cycle = colormaps['tab10']

        # Assign colors, wrapping around if galaxy types exceed 10
        bar_colors = [color_cycle(i % color_cycle.N) for i in range(len(galaxy_type_counts))]


        fig, ax = plt.subplots()
        ax.set_ylim(1, max(galaxy_type_counts.values()) * 1.5)
        bars = ax.bar(
            list(galaxy_type_counts.keys()),
            list(galaxy_type_counts.values()),
            color=bar_colors,
            width=0.5
        )
        ax.bar_label(bars, label_type='edge', padding=2, color='black', fontsize=10)
        ax.set_title(f"Galaxy Type Count of Snapshot {snapshot_num}")
        ax.set_ylabel(r"Number $\longrightarrow$")
        ax.set_xlabel("Galaxy Type")
        ax.tick_params(axis='y', which='major', length=10, direction="in")
        ax.tick_params(axis='y', which='minor', length=5, direction="in")
        ax.set_yscale('log')
        fig.tight_layout()
        try:
            file_name = f"Snap_{snapshot_num}_{output_fname}"
            fig.savefig(file_name, dpi=200)
        except Exception as e:
            print(f"Error saving plot to '{file_name}': {e}")
        if show:
            plt.show()
        plt.close(fig)
        return fig

    def available_snapshots(self) -> List[int]:
        """
        Returns a sorted list of available snapshot numbers.

        Returns:
            List[int]: Sorted list of snapshot numbers.
        """
        return sorted([int(s) for s in self.data["Snapshot"].unique()])


if __name__ == "__main__":
    """
    Example usage of the GalMorph class.
    Loads galaxy morphology data and generates a bar plot for a specific snapshot.
    """
    try:
        GalSim = GalMorph(file_path="data/morphologies_snapshot_data.pkl")
        GalSim.galaxy_type_snap()
    except Exception as e:
        print(f"Error: {e}")