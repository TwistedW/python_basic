import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 50)
y1 = x**2
y2 = x*3+1

plt.figure(num=1)
plt.plot(x, y1)

plt.figure(num=2)
plt.plot(x, y2)
plt.plot(x, y1, color='red', linewidth=1.0, linestyle='--')
plt.show()