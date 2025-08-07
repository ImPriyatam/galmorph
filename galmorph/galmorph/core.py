import pandas as pd
import matplotlib.pyplot as plt

class GalMorph:
    """
    
    """
    def __init__(self, file_path):
        self.data = pd.read_pickle(file_path)

    def _assign_galaxy_type(self, row, thresholds:dict={
    'elliptical': 0.7,'spiral': 0.6,'irregular': 0.5}) -> str:
        """
        Assigns a galaxy type based on the highest value among three input columns.

        Parameters:
            row (pd.Series): A row from a DataFrame, containing columns "P_Spheroid", "P_Disk", & "P_Irr"
            thresholds (dict): Dictionary of critical values, e.g., {'elliptical': 0.7, 'spiral': 0.6, 'irregular': 0.5}
        Returns:
            str: 'elliptical', 'spiral', or 'irregular' depending on which value is highest.
        """
        values = {
            'elliptical': row["P_Spheroid"],
            'spiral': row["P_Disk"],
            'irregular': row["P_Irr"]
        }
        max_type = max(values, key=values.get)
        max_value = values[max_type]
        
        if max_value >= thresholds[max_type]:
            return max_type
        else:
            return 'unknown'

    def Galaxy_count(self, file_name="galaxy_count.png"):
        # print("Running inside the count.....")
        self.snapshot_values = self.data["Snapshot"].drop_duplicates().to_list()
        galaxies_count = []
        for val in self.snapshot_values:
            galaxies_count.append(self.data[self.data["Snapshot"]==val].shape[0])

        plt.figure(figsize = [6, 5])
        plt.plot(self.snapshot_values, galaxies_count, ls = "-.")
        plt.scatter(self.snapshot_values, galaxies_count, marker="o", color = "red")
        plt.minorticks_on()
        plt.xlabel("Snapshot")
        plt.ylabel("Galaxy Count")
        plt.savefig(f"{file_name}", dpi = 130)
        plt.show()

    def Galaxy_type_snap(self, snapshot_num:int=25, output_fname = "bar.png"):
        """
            Plot of Galaxy
        """

        self.data["Galaxy_type"] = self.data.apply(self._assign_galaxy_type, axis=1)
        snapshot_galaxy = self.data[self.data["Snapshot"]==snapshot_num].reset_index()

        galaxy_type_count_dict = {}
        print(snapshot_galaxy["Galaxy_type"].drop_duplicates().values)

        for gal_type in snapshot_galaxy["Galaxy_type"].drop_duplicates().values:
            galaxy_type_count_dict[gal_type] = snapshot_galaxy[snapshot_galaxy["Galaxy_type"] == gal_type].shape[0]

        bar_colors = ['red', 'green', 'blue', 'purple']
        fig, ax = plt.subplots()
        ax.set_ylim(1, 1000)
        # Create the bars and store the BarContainer object
        bars = ax.bar(list(galaxy_type_count_dict.keys()), list(galaxy_type_count_dict.values()), color = bar_colors, width = 0.5)
        # Add labels to the bars
        ax.bar_label(bars, label_type='edge', padding=2, color='black', fontsize=10)
        ax.set_title(f"Galaxy Type Count of Snapshot {snapshot_num}")
        ax.set_ylabel(r"Number $\longrightarrow$")
        ax.set_xlabel("Galaxy Type")
        ax.tick_params(axis='y', which = 'major', length = 10, direction = "in")
        ax.tick_params(axis='y', which = 'minor', length = 5, direction = "in")
        ax.set_yscale('log')
        print(ax.get_ylim())
        plt.savefig(f"{output_fname}", dpi = 200)
        plt.show()


if __name__ == "__main__":
    GalSim = GalMorph(file_path="galmorph/data/morphologies_snapshot_data.pkl")
    GalSim.Galaxy_type_snap()
