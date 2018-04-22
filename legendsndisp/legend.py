import numpy as np
import matplotlib.pyplot as plt

# Make some fake data.
a = b = np.arange(0, 3, .09)
c = np.exp(a)
d = c[::-1]

# Create plots with pre-defined labels.
fig, ax = plt.subplots()
stdDev= 0.5
ax.errorbar(a, c,  yerr=stdDev,capsize=4,  label='Model length', linestyle='-.', color='r')
ax.errorbar(a, d, yerr=stdDev, lolims=stdDev ,label='Data length', linestyle=':', color='#00CC00')
ax.errorbar(a, c + d,yerr=stdDev, uplims=stdDev,label='Total message length',color='#6eb5ef')

legend = ax.legend(loc='upper center',bbox_to_anchor=(0.5, 1), shadow=True, fontsize='x-large')

legend.get_frame().set_facecolor('#fff575')

plt.show()
