import matplotlib.pyplot as plt
import numpy as np

# Dataset: https://data.giss.nasa.gov/gistemp/
# Global Mean Estimates Based on Land-Surface Air Temperature Anomalies Only (Meteorological Station Data, dTs)
# Global-mean monthly, seasonal, and annual means, 1880-present, updated through most recent month
# DJA: December, January, February
# MAM: March, April, May
# JJA: June, July, August
# SON: September, October, November
# anual mean == vector[13]

M = []
with open("GLB.Ts.csv", "r") as fileReader:
    lines = fileReader.readlines()
M = np.array([line.split(',')[13] for line in lines], dtype=float)

plt.figure(figsize=(16, 14))
years = np.arange(1880, 2018, 1)
plt.title("Global Mean Estimates Based on Land-Surface Air Temperature ")
plt.plot(years, M.T, label='Estimated Global Mean', ls='--', c='b', marker='*', markersize=5, markeredgecolor='r')
plt.grid(True)
plt.axes().set_xticks(years, minor=True)
plt.ylabel("°C")
plt.xlabel("YEARS")
plt.legend(loc='upper left', bbox_to_anchor=(0, 1), fontsize='x-large', facecolor='white', fancybox=True, framealpha=1)
plt.show()
