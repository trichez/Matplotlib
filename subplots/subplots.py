import numpy as np
import matplotlib.pyplot as plt


plt.figure('subplots')
plt.style.use('classic')
stdDev= 0.1
# Make some fake data.
a = b = np.arange(0, 10, .09)
c = np.sin(a)
b = np.cos(a)
d = c[::-1]

plt.subplot(2,2,1)
handler1 = plt.errorbar(a, c,  xerr=stdDev*3,capsize=4,  label='Model length' , color='r')


plt.subplot(2,2,2)
handler2 =  plt.errorbar(a, d, yerr=stdDev, lolims=stdDev ,label='Data length', linestyle=':', color='#00CC00')


plt.subplot(2,2,3)
handler3 = plt.errorbar(a,b,yerr=stdDev, uplims=stdDev,label='Total message length',linestyle='--', color='#6eb5ef')



plt.legend(handles=[handler1,handler2,handler3],loc='center', bbox_to_anchor=(1.75, 0.5), shadow=True, fontsize='x-large')

plt.show()
