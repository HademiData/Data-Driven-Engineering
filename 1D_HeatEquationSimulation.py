import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# Simulation parameters
# -----------------------------
alpha = 110            # Thermal diffusivity (mm^2/s)
rod_length = 50        # Length of the rod in mm
total_time = 4         # Total simulation time in seconds
num_points = 20        # Number of spatial divisions along the rod

# -----------------------------
# Discretization
# -----------------------------
dx = rod_length / (num_points - 1)     # Spatial step size
dt = 0.5 * dx**2 / alpha               # Time step (for stability)
time_steps = int(total_time / dt) + 1  # Number of time iterations

# -----------------------------
# Initial temperature distribution
# -----------------------------
temperature = np.full(num_points, 20.0)  # Initial uniform temperature (°C)

# -----------------------------
# Boundary conditions
# -----------------------------
temperature[0] = 100.0   # Left end
temperature[-1] = 100.0  # Right end

# -----------------------------
# Plot setup
# -----------------------------
fig, ax = plt.subplots()
color_map = ax.pcolormesh([temperature], cmap='jet', vmin=0, vmax=100)
plt.colorbar(color_map, ax=ax)
ax.set_ylim([-2, 3])

# -----------------------------
# Time stepping loop
# -----------------------------
elapsed_time = 0.0

while elapsed_time < total_time:
    prev_temp = temperature.copy()
    
    # Update interior points using explicit finite difference
    for j in range(1, num_points - 1):
        temperature[j] = prev_temp[j] + (alpha * dt / dx**2) * (
            prev_temp[j - 1] - 2 * prev_temp[j] + prev_temp[j + 1]
        )

    elapsed_time += dt
    print(f"t: {elapsed_time:.3f} s, Mean Temp: {np.mean(temperature):.2f} °C")

    # Update the plot in real time
    color_map.set_array([temperature])
    ax.set_title(f"Temperature profile at t = {elapsed_time:.3f} s")
    plt.pause(0.01)

plt.show()
