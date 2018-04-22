import numpy as np
import matplotlib.pyplot as plt

# Make some fake data.
a = b = np.arange(0, 3, .09)
c = np.exp(a)
d = c[::-1]

# Create plots with pre-defined labels.
plt.figure("Legend")
stdDev= 0.5
plt.errorbar(a, c,  yerr=stdDev,capsize=4,  label='Model length', linestyle='-.', color='r')
plt.errorbar(a, d, yerr=stdDev, lolims=stdDev ,label='Data length', linestyle=':', color='#00CC00')
plt.errorbar(a, c + d,yerr=stdDev, uplims=stdDev,label='Total message length',color='#6eb5ef')

legend = plt.legend(loc='upper center',bbox_to_anchor=(0.5, 1), shadow=True, fontsize='x-large')

legend.get_frame().set_facecolor('#fff575')

plt.show()
