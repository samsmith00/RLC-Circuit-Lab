import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from numpy.linalg import eig
import math
import random

# Define random parameter generation
HIGH = 10
LOW = 0.1


def underdamped():
    def generate_underdamped_parameters(): 
        C, L = get_random_parameters()

        R_max = math.sqrt(4 * L / C)
        R = np.random.uniform(0.1, R_max)

        return R, C, L

    # Have the characteristic polynomial be less than 0. 
    R, C, L = generate_underdamped_parameters()

    A = np.array([[0, 1/C], 
                  [-1/L, -R/C]])

    eigenvals, eigenvects = eig(A)


     



def get_random_parameters(): 
    R = random.uniform(LOW, HIGH)
    C = random.uniform(LOW, HIGH)
    L = random.uniform(LOW, HIGH)
    return [R, C, L]

# Define the system of equations
def system(t, y, R, C, L): 
    vc = y[0]
    i = y[1]
    
    # Equation 1
    dvc_dt = i / C 

    #Equation 2
    di_dt = -(R * i + vc) / L 
    
    return [dvc_dt, di_dt]  #

# Plot phase portrait with vector field
def plot_phase_portrait(t_span, initial_conditions): 
    t_eval = np.linspace(t_span[0], t_span[1], 1000)  # Fine-grained time points
    plt.figure(figsize=(10, 8))

    # Generate grid for vector field
    vc_vals = np.linspace(-2, 2, 20)  
    i_vals = np.linspace(-2, 2, 20)  
    vc_grid, i_grid = np.meshgrid(vc_vals, i_vals)

    # Initialize vector field
    dvc_grid = np.zeros_like(vc_grid)
    di_grid = np.zeros_like(i_grid)

    # Use fixed parameters for vector field
    R, C, L = get_random_parameters()

    for x in range(vc_grid.shape[0]):
        for y in range(vc_grid.shape[1]):
            derivatives = system(0, [vc_grid[x, y], i_grid[x, y]], R, C, L)
            dvc_grid[x, y], di_grid[x, y] = derivatives

    # Normalize vectors for uniform arrow lengths
    magnitude = np.sqrt(dvc_grid**2 + di_grid**2)
    dvc_grid /= magnitude
    di_grid /= magnitude

    # Plot vector field
    plt.quiver(vc_grid, i_grid, dvc_grid, di_grid, color='lightblue', alpha=0.8)

    # Overlay phase trajectories
    for initial_condition in initial_conditions: 
        solution = solve_ivp(
            system, 
            t_span, 
            initial_condition, 
            t_eval=t_eval, 
            args=(R, C, L)
        )
        plt.plot(solution.y[0], solution.y[1], label=f"Initial: {initial_condition}")
    
    # Add labels, grid, and legend
    plt.xlabel('Voltage across Capacitor (vC)')
    plt.ylabel('Current (i)')
    plt.title('Phase Portrait with Vector Field of the RL-C Circuit')
    plt.axhline(0, color='black', linewidth=1)
    plt.axvline(0, color='black', linewidth=1)
    plt.grid(True)
    plt.legend()
    plt.show()

# Time span and initial conditions
t_span = [0, 15]  # Start and end time
initial_conditions = [
    [1, 0],  
    [0, 1],
    [2, -1],
    [-1, 2]
]

# Generate the enhanced phase portrait
plot_phase_portrait(t_span, initial_conditions)
