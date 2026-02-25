import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Create figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

# Create circle
circle = plt.Circle((0, 5), 0.5, color='blue')
ax.add_patch(circle)

# Animation function
def update(frame):
    circle.center = (frame, 5)   # Move circle along x-axis
    return circle,

# Create animation
ani = FuncAnimation(fig, update, frames=np.linspace(0, 10, 100),
                    interval=50, blit=True)

plt.title("Moving Circle Animation")
plt.show()
