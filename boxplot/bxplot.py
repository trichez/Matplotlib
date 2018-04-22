import matplotlib.pyplot as plt
import numpy as np
# figures: http://www.physics.csbsju.edu/stats/box2.html

np.random.seed(100)
# Create some fake data
collectn_1 = np.random.normal(100, 10, 200)
collectn_2 = np.random.normal(80, 30, 200)
collectn_3 = np.random.normal(90, 20, 200)
collectn_4 = np.random.normal(70, 25, 200)
collectn_5 = np.random.normal(70, 25, 200)
#np.random.normal(mean, stdDev, n)
data_to_plot = [collectn_1, collectn_2, collectn_3, collectn_4]

plt.figure("First 4 data collections")
plt.boxplot(data_to_plot, 1)
ax = plt.axes()
ax.set_xticklabels(['Collection 1', 'Collection 2', 'Collection 3', 'Collection 4'])


plt.figure("Last data collection in a notched boxplot")
plt.boxplot(collectn_5, 0)
plt.grid(ls='--')
ax = plt.axes()
ax.set_xticklabels(['Collection 5'])


plt.show()
