import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def ambilibrium_system(y, t, alpha=0.1):
    """
    Defines the system of differential equations for Ambilibrium.
    y[0] = y1, y[1] = y2
    This system creates a stable limit cycle.
    """
    y1, y2 = y
    
    # A simple oscillator with a non-linear term to create a limit cycle
    # This enforces a stable, dynamic tension rather than collapse or divergence.
    d_y1_dt = y2 + alpha * y1 * (1 - y1**2 - y2**2)
    d_y2_dt = -y1 + alpha * y2 * (1 - y1**2 - y2**2)
    
    return [d_y1_dt, d_y2_dt]

def plot_ambilibrum_attractor():
    """
    Solves and plots the phase-space for the Ambilibrium system.
    """
    # Time points and initial conditions
    t = np.linspace(0, 100, 2000)
    y0 = [0.5, 0.5] # Starting point

    # Solve the ODE
    solution = odeint(ambilibrum_system, y0, t)
    
    # Plotting
    plt.figure(figsize=(8, 8))
    plt.plot(solution[:, 0], solution[:, 1], lw=2)
    plt.title('Ambilibrium Attractor (Phase-Space Diagram)', fontsize=16)
    plt.xlabel('Opposite State (y1)', fontsize=12)
    plt.ylabel('Opposite State (y2)', fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.axis('equal')
    plt.show()

# Run the function
plot_ambilibrum_attractor()