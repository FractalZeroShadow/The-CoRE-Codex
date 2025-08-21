import numpy as np
import matplotlib.pyplot as plt

def generate_bifurcation_diagram():
    """
    Generates and plots the logistic map bifurcation diagram.
    """
    # Parameters
    n_iterations = 1000  # Number of iterations for each r value
    n_last_to_plot = 100 # Number of final points to plot to show attractors
    r_min, r_max = 2.5, 4.0 # Range of the bifurcation parameter r
    n_r_steps = 4000     # Number of r values to simulate

    # Create an array of r values
    r_values = np.linspace(r_min, r_max, n_r_steps)
    
    # Initialize x and run the simulation
    x = 0.2 * np.ones(n_r_steps) # Initial condition for each r
    
    # Iterate to allow the system to settle into its attractor
    for _ in range(n_iterations - n_last_to_plot):
        x = r_values * x * (1 - x)

    # Store the attractor points
    attractor_points_x = []
    attractor_points_y = []

    # Collect the final points for plotting
    for _ in range(n_last_to_plot):
        x = r_values * x * (1 - x)
        attractor_points_x.extend(r_values)
        attractor_points_y.extend(x)
        
    # Plotting
    plt.figure(figsize=(12, 8))
    plt.plot(attractor_points_x, attractor_points_y, ',k', alpha=0.1)
    plt.title('Logistic Map Bifurcation Diagram', fontsize=16)
    plt.xlabel('Bifurcation Parameter (r)', fontsize=12)
    plt.ylabel('Attractor Values (x)', fontsize=12)
    plt.xlim(r_min, r_max)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.show()

# Run the function
generate_bifurcation_diagram()