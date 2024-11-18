import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Create figure
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Parameters for the cylinder
x = np.linspace(0, 10, 100)  # Cylinder's axis (x-axis)
theta = np.linspace(0, 2 * np.pi, 50)  # Angular points for the circular base
r = 1  # Radius of the cylinder

# Create mesh for cylinder
X, T = np.meshgrid(x, theta)
Y = r * np.cos(T)  # Circular cross-section along Y
Z = r * np.sin(T)  # Circular cross-section along Z

# Plot cylinder
ax.plot_surface(X, Y, Z, color='white', alpha=0.6, edgecolor='none')

# Plot the temperature gradient T(x)
T_x = x  # For simplicity, assume T(x) = x (linear)
ax.plot(x, np.zeros_like(x), np.zeros_like(x), color='orange', linewidth=2, label='T(x)')

# Customize axes
ax.set_xlabel('X', color='gold')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Adjust the background color to dark mode
ax.set_facecolor('#1E1E1E')  # Dark mode background
fig.patch.set_facecolor('#1E1E1E')  # Set the figure background to dark

# Hide pane borders
ax.xaxis.pane.fill = False
ax.yaxis.pane.fill = False
ax.zaxis.pane.fill = False

# Hide gridlines
ax.grid(False)

plt.legend()
plt.show()
