import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# Simulation setup
# -----------------------------
alpha = 110             # Thermal diffusivity (mm^2/s)
plate_size = 50         # Side length of the plate (mm)
simulation_time = 4     # Total time for simulation (seconds)
grid_points = 40        # Number of grid points along one dimension

# -----------------------------
# Discretization
# -----------------------------
dx = plate_size / (grid_points - 1)
dy = plate_size / (grid_points - 1)

# Time step (stability condition)
dt = min(dx**2 / (4 * alpha), dy**2 / (4 * alpha))
total_steps = int(simulation_time / dt) + 1

# -----------------------------
# Initial temperature field
# -----------------------------
temp_field = np.full((grid_points, grid_points), 20.0)  # Initial uniform temperature

# -----------------------------
# Boundary conditions
# -----------------------------
temp_field[0, :]  = np.linspace(0, 100, grid_points)  # Top edge
temp_field[-1, :] = np.linspace(0, 100, grid_points)  # Bottom edge
temp_field[:, 0]  = np.linspace(0, 100, grid_points)  # Left edge
temp_field[:, -1] = np.linspace(0, 100, grid_points)  # Right edge

# -----------------------------
# Visualization setup
# -----------------------------
fig, ax = plt.subplots()
heatmap = ax.pcolormesh(temp_field, cmap='jet', vmin=0, vmax=100)
plt.colorbar(heatmap, ax=ax)

# -----------------------------
# Time-stepping loop
# -----------------------------
elapsed_time = 0.0

while elapsed_time < simulation_time:
    prev_temp = temp_field.copy()
    
    # Update interior points using explicit finite difference
    for i in range(1, grid_points - 1):
        for j in range(1, grid_points - 1):
            d2x = (prev_temp[i-1, j] - 2*prev_temp[i, j] + prev_temp[i+1, j]) / dx**2
            d2y = (prev_temp[i, j-1] - 2*prev_temp[i, j] + prev_temp[i, j+1]) / dy**2
            temp_field[i, j] = prev_temp[i, j] + alpha * dt * (d2x + d2y)

    elapsed_time += dt
    print(f"t: {elapsed_time:.3f} s, Mean Temp: {np.mean(temp_field):.2f} °C")

    # Update visualization
    heatmap.set_array(temp_field.ravel())
    ax.set_title(f"Temperature distribution at t = {elapsed_time:.3f} s")
    plt.pause(0.01)

plt.show()
