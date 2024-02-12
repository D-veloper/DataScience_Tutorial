import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

axis = plt.axes(projection="3d")

# z = np.linspace(0, 30, 100)
# x = np.sin(z)
# y = np.cos(z)

def z_function(x, y):
    return np.sin(np.sqrt(x ** 2 + y ** 2))

x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)

X, Y = np.meshgrid(x, y)
Z = z_function(X, Y)

axis.plot_surface(X, Y, Z)

plt.show()
