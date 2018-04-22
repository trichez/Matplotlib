import matplotlib.pyplot as plt
import numpy as np

# raw data from: https://github.com/plotly/datasets/blob/master/Canada%20Immigration.csv
M = []
with open("data.csv", "r") as fileReader:
    lines = fileReader.readline()
    lines = fileReader.readlines()
M = np.array([line.split(',') for line in lines], dtype=int)
M = M.T
X = M[0:M.shape[0]][0]
Y1 = M[0:M.shape[0]][3]
Y2 = M[0:M.shape[0]][4]

plt.figure("Subplots Exercise")


plt.subplot(2,1,1)
plt.title("Subplots Exercise")
plt.errorbar(X, Y1, yerr=np.std(Y1), capsize=4, linestyle='-.', color='#008406')
plt.ylabel("measurement")
plt.xlabel("time")

plt.subplot(2,1,2)
plt.errorbar(X, Y2, yerr=np.std(Y2), capsize=4, linestyle='--', color='#ba0331')
plt.xlabel("time")
plt.ylabel("measurement")


plt.show()
