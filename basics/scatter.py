import numpy as np
import matplotlib.pyplot as plt

# Fixing random state for reproducibility
np.random.seed(19680801)
plt.rcParams['axes.xmargin'] = 0
plt.rcParams['axes.ymargin'] = 0

N = 50
x = np.random.rand(N)
y = np.random.rand(N)

colors = np.random.rand(N) #A sequence of color specifications of length N
area = np.pi * (15 * np.random.rand(N))**2  #size of the marker

plt.scatter(x, y, s=area, c=colors, alpha=0.5)
plt.grid(color='k', linestyle='--', linewidth=1)

plt.show()
