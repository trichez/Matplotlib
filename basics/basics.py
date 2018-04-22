import matplotlib.pyplot as plt
import numpy as np



x = np.linspace(0, 2, 100) # Returns num evenly spaced samples, calculated over the interval [start, stop].

plt.figure(1)
#linestyles: solid’ | ‘dashed’, ‘dashdot’, ‘dotted’
plt.plot(x, x, linestyle='--', c='#FF0000' )
plt.plot(x, x**2, linestyle=':', c='b')
plt.plot(x, x**3, linestyle='-.', c='turquoise')

plt.xlabel('x label')
plt.ylabel('y label')
plt.title("Simple Plot")


plt.show()


# -------------------------------------------
plt.figure("Savefig example", figsize=(14, 10))

plt.plot(x, x, marker='*', markersize=7)
plt.plot(x, x**2, marker='D', markersize=5, markerfacecolor='b')
plt.plot(x, x**3, marker='8', markersize=7)

plt.xlabel('x label')
plt.ylabel('y label')
plt.title("Simple Plot")


plt.savefig("example.png")
