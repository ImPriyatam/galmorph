import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


df_loaded = pd.read_pickle("morphologies_snapshot_data.pkl")
# df_loaded = pd.read_csv("galaxies_morph.csv")
# print(df_loaded.dtypes)
# print(df_loaded.columns)

snapshot_values = df_loaded["Snapshot"].drop_duplicates().to_list()
galaxies_count = []
for val in snapshot_values:
    # print(val, ":", df_loaded[df_loaded["Snapshot"]==val].shape[0])
    galaxies_count.append(df_loaded[df_loaded["Snapshot"]==val].shape[0])

plt.figure(figsize = [6, 4])
plt.plot(snapshot_values, galaxies_count)
plt.show()
