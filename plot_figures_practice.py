from matplotlib import pyplot as plt
import numpy as np

# draw a circle
theta = np.arange(0, 2*np.pi, 0.1)
r = 5
x = r*np.cos(theta)
y = r*np.sin(theta)
x = np.append(x, x[0])
y = np.append(y, y[0])
plt.plot(x, y)
# plt.scatter(x, y)
plt.axis('equal')
plt.show()
