# 🎢 Double Pendulum Simulation using Lagrangian Mechanics

This project models and simulates the motion of a **double pendulum system** using **Lagrangian mechanics**. The double pendulum is a classic example of a **chaotic, nonlinear system**, meaning its motion is highly sensitive to initial conditions and exhibits complex dynamics even though the underlying physics is deterministic.

We derive the system's **equations of motion symbolically** using the **Euler-Lagrange equations**, solve them numerically using `SciPy`, and **animate** the resulting motion using `Matplotlib`.

---

## 📘 Problem Concept

The double pendulum consists of two point masses \( m_1 \) and \( m_2 \) suspended by rigid, massless rods of lengths \( l_1 \) and \( l_2 \). The upper pendulum is attached to a fixed pivot, and the second pendulum is attached to the end of the first.

This system is governed by Newtonian physics, but instead of applying Newton’s second law directly, we use the **Lagrangian formulation** to derive equations of motion based on the system's kinetic and potential energy.

---

## 🧮 Lagrangian Mechanics

### Coordinates:
We use two angular coordinates:
- \( \theta_1(t) \): Angle of the first pendulum from the vertical
- \( \theta_2(t) \): Angle of the second pendulum from the vertical

### Position of masses:
\[
\begin{align*}
x_1 &= l_1 \sin(\theta_1), & y_1 &= -l_1 \cos(\theta_1) \\
x_2 &= x_1 + l_2 \sin(\theta_2), & y_2 &= y_1 - l_2 \cos(\theta_2)
\end{align*}
\]

### Kinetic Energy \( T \):
\[
T = \frac{1}{2} m_1 (\dot{x}_1^2 + \dot{y}_1^2) + \frac{1}{2} m_2 (\dot{x}_2^2 + \dot{y}_2^2)
\]

### Potential Energy \( V \):
\[
V = m_1 g y_1 + m_2 g y_2
\]

### Lagrangian \( \mathcal{L} \):
\[
\mathcal{L} = T - V
\]

### Euler-Lagrange Equation:
For each \( \theta_i \):
\[
\frac{d}{dt} \left( \frac{\partial \mathcal{L}}{\partial \dot{\theta}_i} \right) - \frac{\partial \mathcal{L}}{\partial \theta_i} = 0
\]

These equations are converted to a first-order ODE system and solved numerically.

---

## 📦 Dependencies

Install the following Python libraries:

```bash
pip install numpy sympy scipy matplotlib
