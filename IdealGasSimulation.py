import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')  # Use TkAgg backend for interactive plotting


# P = nRT/V
# n = N/N_A

# --- Simulation Parameters ---
NUM_PARTICLES = 100         # Number of gas particles
CONTAINER_SIZE = 10         # Length of the 2D square container
TIME_STEPS = 1000           # Number of simulation steps
PARTICLE_SPEED = 0.5        # Approximate constant speed of particles

# --- Initialize Particle States ---
# Random initial positions within the container
positions = np.random.rand(NUM_PARTICLES, 2) * CONTAINER_SIZE

# Random initial velocities scaled to approximate temperature
velocities = np.random.rand(NUM_PARTICLES, 2) * PARTICLE_SPEED

# --- Set up Visualization ---
fig, ax = plt.subplots()
scatter = ax.scatter(positions[:, 0], positions[:, 1], marker='o')
ax.set_xlim(0, CONTAINER_SIZE)
ax.set_ylim(0, CONTAINER_SIZE)
ax.set_aspect('equal', adjustable='box')
plt.grid(True)

# --- Simulation Loop ---
collision_counts = []

for step in range(TIME_STEPS):
    # Update positions based on velocities
    positions += velocities

    collisions_in_step = 0

    # Check and handle collisions with walls
    for i in range(NUM_PARTICLES):
        for dim in range(2):  # 0 = x, 1 = y
            if positions[i, dim] < 0 or positions[i, dim] > CONTAINER_SIZE:
                velocities[i, dim] *= -1  # Reflect velocity (bounce)
                collisions_in_step += 1

    # Record number of collisions for this step
    collision_counts.append(collisions_in_step)

    # Display average number of collisions over time
    avg_collisions = np.mean(collision_counts)
    print(f"Step {step+1}/{TIME_STEPS} | Collisions: {collisions_in_step} | Average: {avg_collisions:.2f}", end='\r')

    # Stop if plot window is closed
    if not plt.fignum_exists(fig.number):
        break

    # Update scatter plot with new positions
    scatter.set_offsets(positions)
    plt.pause(0.001)

plt.show()
