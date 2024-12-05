import numpy as np
import matplotlib.pyplot as plt

# Parameters
domain_length = 1.0  # Length of the 1D domain
nx_low = 55         # Number of points in low-resolution grid
nx_high = nx_low * 5 - 1       # Number of points in high-resolution grid
dt = 0.01            # Time step
nt = 100           # Number of time steps
velocity = 0.1       # Constant advection velocity

# High-resolution and low-resolution grids
x_high = np.linspace(0, domain_length, nx_high)
x_low = np.linspace(0, domain_length, nx_low)
dx_high = x_high[1] - x_high[0]
dx_low = x_low[1] - x_low[0]

# Initial damage field (step function)
damage_low = np.piecewise(x_low, [x_low < 0.5, x_low >= 0.5], [0.2, 0.8])

# Interpolate high-resolution damage to low resolution as an initial damage
damage_high  = np.interp(x_high, x_low, damage_low)

# Function to advect damage using finite differences
def advect_damage(damage, velocity, dx, dt):
    advected_damage = np.copy(damage)
    for i in range(1, len(damage) - 1):  # Exclude boundaries for simplicity
        advected_damage[i] -= velocity * dt / dx * (damage[i] - damage[i - 1])
    return advected_damage

# Store initial conditions for comparison
initial_damage_high = np.copy(damage_high)
initial_damage_low = np.copy(damage_low)

# Main simulation loop
for t in range(nt):
    # Advect damage field on high resolution
    damage_high = advect_damage(damage_high, velocity, dx_high, dt)
    damage_low = advect_damage(damage_low, velocity, dx_low, dt)

# Plot results
fig, axs = plt.subplots(3, 1, figsize=(10, 12))

# Initial vs final high-resolution damage field
axs[0].plot(x_high, initial_damage_high, label="Initial Damage (High Res)", color="blue", linestyle="--")
axs[0].plot(x_high, damage_high, label="Final Damage (High Res)", color="blue")
axs[0].set_ylabel("Damage")
axs[0].set_title("High-Resolution Damage Field: Initial vs Final")
axs[0].legend()

# Initial vs final low-resolution damage field
axs[1].plot(x_low, initial_damage_low, label="Initial Damage (Low Res)", color="orange", linestyle="--")
axs[1].plot(x_low, damage_low, label="Final Damage (Low Res)", color="orange")
axs[1].set_ylabel("Damage")
axs[1].set_title("Low-Resolution Damage Field: Initial vs Final")
axs[1].legend()

# Final high-resolution vs low-resolution damage field
axs[2].plot(x_high, damage_high, label="Final Damage (High Res)", color="blue")
axs[2].plot(x_low, damage_low, 'o-', label="Final Damage (Low Res)", color="orange")
axs[2].set_ylabel("Damage")
axs[2].set_xlabel("x (1D domain)")
axs[2].set_title("Comparison of Final Damage: High vs Low Resolution")
axs[2].legend()

plt.tight_layout()
plt.savefig('2_Mesh_Concept.png')