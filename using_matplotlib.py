import numpy as np
import matplotlib.pyplot as plt

# Section 1 - Plotting a single function.

# x_values = np.arange(-100, 101, 1)
#
# y_values = 3 * (x_values ^ 3) + 2 * (x_values ^ 2) + x_values

# plt.plot(x_values, y_values, 'r--')  # third argument to customize graph aesthetic.

# plt.show()

# Section 2 - Plotting multiple functions in the same window.
#   Section 2.1. Plotting with actual functions.
# def eq_1(x, y):
#     return np.square(x) - y + np.sin(x)/(np.tan(y) + 0.1)
#
#
# def eq_2(x, y, z):
#     return np.square(y) - z + np.sin(y)/(np.cos(x) + 0.1)
#
#
# #   Generate a grid of x and y values
# x_val = np.arange(-10, 10, 1)
# y_val = np.arange(-10, 10, 1)
#
# x_val, y_val = np.meshgrid(x_val, y_val)  # create a meshgrid for the x and y values
#
# z1_val = eq_1(x_val, y_val)
# z2_val = eq_2(x_val, y_val, z1_val)
#
# plt.contour(x_val, y_val, z1_val, colors='red')
# plt.contour(x_val, y_val, z2_val, colors='blue')
#
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')
# plt.title('Multiplot Demo')
#
# plt.show()

#   Section 2.2 Plotting with coordinates

x = np.arange(-100, 100, 1)
y1 = (3 * np.square(x) - 2 * x + 3) * 50
y2 = np.square(x) * x + 2 * np.square(x)/(np.sin(x) - 0.01)
#
# plt.plot(x, y1, 'r')
# plt.plot(x, y2)
# plt.show()

# Section 3 - Plotting Subplots in the same window
ax1 = plt.subplot(211)  # no. of rows in window, no. of columns, index of the subplot.
ax2 = plt.subplot(212)

ax1.plot(x, y1)
ax2.plot(x, y2)
plt.tight_layout()  # for better spacing in plot layout
plt.show()

# Section 4 - Plotting in multiple windows.
#   same as normal plotting but add plt.figure(table_number) at the top to create a new window.
