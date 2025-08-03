import numpy as np
import sympy as sm
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define symbols and constants
t = sm.symbols('t')
m_1, m_2, g = sm.symbols('m_1 m_2 g', positive=True)
theta1, theta2 = sm.symbols('theta1 theta2', cls=sm.Function)
theta1 = theta1(t)
theta2 = theta2(t)

# Cartesian coordinates for each mass
x1 = sm.sin(theta1)
y1 = -sm.cos(theta1)
x2 = x1 + sm.sin(theta2)
y2 = y1 - sm.cos(theta2)

# First and second derivatives
theta1_d = sm.diff(theta1, t)
theta2_d = sm.diff(theta2, t)
theta1_dd = sm.diff(theta1_d, t)
theta2_dd = sm.diff(theta2_d, t)

x1_d = sm.diff(x1, t)
y1_d = sm.diff(y1, t)
x2_d = sm.diff(x2, t)
y2_d = sm.diff(y2, t)

# Energies
T1 = 0.5 * m_1 * (x1_d**2 + y1_d**2)
T2 = 0.5 * m_2 * (x2_d**2 + y2_d**2)
V1 = m_1 * g * y1
V2 = m_2 * g * y2

# Lagrangian
L = (T1 + T2) - (V1 + V2)

# Euler-Lagrange equations
LE1 = sm.diff(sm.diff(L, theta1_d), t) - sm.diff(L, theta1)
LE2 = sm.diff(sm.diff(L, theta2_d), t) - sm.diff(L, theta2)

# Solving the system
sol = sm.solve([LE1, LE2], (theta1_dd, theta2_dd))
f1 = sm.lambdify((theta1, theta2, theta1_d, theta2_d, t, m_1, m_2, g), sol[theta1_dd])
f2 = sm.lambdify((theta1, theta2, theta1_d, theta2_d, t, m_1, m_2, g), sol[theta2_dd])

# Initial state and constants
initial_state = [1.0, 0.0, 1.0, 0.0]  # [theta1, theta1_dot, theta2, theta2_dot]
m1_val, m2_val, g_val = 2, 4, 9.81

# ODE system definition
def pendulum_ode(state, t, m1, m2, g):
    th1, th1_d, th2, th2_d = state
    th1_dd = f1(th1, th2, th1_d, th2_d, t, m1, m2, g)
    th2_dd = f2(th1, th2, th1_d, th2_d, t, m1, m2, g)
    return [th1_d, th1_dd, th2_d, th2_dd]

# Time vector
time = np.linspace(0, 40, 1001)

# Solve system
solution = odeint(pendulum_ode, initial_state, time, args=(m1_val, m2_val, g_val))
th1_vals, th2_vals = solution[:, 0], solution[:, 2]

# Convert to Cartesian coordinates
x1_vals = np.sin(th1_vals)
y1_vals = -np.cos(th1_vals)
x2_vals = x1_vals + np.sin(th2_vals)
y2_vals = y1_vals - np.cos(th2_vals)

# Animation setup
def update(frame):
    pendulum1.set_data([0, x1_vals[frame]], [0, y1_vals[frame]])
    mass1.set_data([x1_vals[frame]], [y1_vals[frame]])
    pendulum2.set_data([x1_vals[frame], x2_vals[frame]], [y1_vals[frame], y2_vals[frame]])
    mass2.set_data([x2_vals[frame]], [y2_vals[frame]])
    return pendulum1, mass1, pendulum2, mass2

fig, ax = plt.subplots()
ax.set_xlim(-3, 3)
ax.set_ylim(-3, 1)
plt.grid()

pendulum1, = ax.plot([], [], lw=2)
mass1, = ax.plot([], [], 'o', markersize=4*m1_val+1, color="red")
pendulum2, = ax.plot([], [], lw=2)
mass2, = ax.plot([], [], 'o', markersize=4*m2_val+1, color="blue")

ani = FuncAnimation(fig, update, frames=len(time), interval=25, blit=True)
plt.show()
