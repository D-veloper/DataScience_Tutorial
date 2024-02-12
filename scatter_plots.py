import numpy as np
import matplotlib.pyplot as plt

height_cm = np.random.randint(150, 180, 20)
weight_kg = np.random.randint(45, 90, 20)

plt.scatter(height_cm, weight_kg, c='red', marker='2', s=150)
plt.show()
