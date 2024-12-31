import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from numpy.linalg import eig

HIGH = 10
LOW = 0.1

def system(t, y, R, C, L): 
    vc = y[0]  # Voltage across the capacitor
    i = y[1]   # Current through the circuit
    
    #Equation 1 
    dvc_dt = i / C 

    # Equation 2
    di_dt = -(R * i + vc) / L  
    
    return [dvc_dt, di_dt]  

# Define the stream plot function
def plot_stream_system(system, R, C, L):
    # Create a grid in phase space
    vc = np.linspace(-7, 7, 20)  
    i = np.linspace(-7, 7, 20)   
    VC, I = np.meshgrid(vc, i)
    
    # Calculate derivatives
    dVC_dt, dI_dt = np.zeros(VC.shape), np.zeros(I.shape)
    for row in range(VC.shape[0]):
        for col in range(VC.shape[1]):
            derivatives = system(0, [VC[row, col], I[row, col]], R, C, L)
            dVC_dt[row, col] = derivatives[0]
            dI_dt[row, col] = derivatives[1]
    
    # get time and solutions
    solution = solve_ivp(system, t_span, initial_conditions, args=(R, C, L), dense_output=True)
    t = np.linspace(t_span[0], t_span[1], 500)
    y = solution.sol(t)
    
    # Plot streamlines
    plt.figure(figsize=(8, 6))
    plt.streamplot(VC, I, dVC_dt, dI_dt, color="blue", linewidth=1)
    plt.plot(y[0], y[1], color="red", label="Solution trajectory", linewidth=2)
    plt.title("Phase Space (Stream Plot)")
    plt.xlabel("Voltage across Capacitor ($v_C$)")
    plt.ylabel("Current ($i$)")
    plt.grid()
    plt.show()

# Get solution graph function
def plot_solution_graph(system, R, C, L, initial_conditions, t_span):
    # Solve the system of ODEs
    solution = solve_ivp(system, t_span, initial_conditions, args=(R, C, L), dense_output=True)
    
    # Extract time and solutions
    t = np.linspace(t_span[0], t_span[1], 500)
    y = solution.sol(t)

    #Debugging 
    A = np.array([[0, 1/C], 
                  [-1/L, -R/C]])

    eigenvals, eigenvects = eig(A)
    print("Eigenvalues: ", eigenvals)
    
    # Plot voltage and current over time
    plt.figure(figsize=(10, 6))
    plt.plot(t, y[0], label="$v_C(t)$ (Voltage across Capacitor)")
    plt.plot(t, y[1], label="$i(t)$ (Current through Circuit)")
    plt.title("Solution Graphs for Underdamped System")
    plt.xlabel("Time (t)")
    plt.ylabel("State Variables")
    plt.axhline(0, color="black", linewidth=1, linestyle="--", label="x-axis")  # Horizontal axis
    plt.axvline(0, color="black", linewidth=1, linestyle="--", label="y-axis")  # Vertical axis
    plt.legend()
    plt.grid()
    plt.show()

def get_random_parameters(): 
    #R = np.random.uniform(LOW, HIGH)
    C = np.random.uniform(LOW, HIGH)
    L = np.random.uniform(LOW, HIGH)
    return [C, L]

# Get underdamped parameters
def generate_underdamped_parameters(): 
        C, L = get_random_parameters()

        R_max = np.sqrt(4 * L / C)
        R = np.random.uniform(0.1, R_max)

        return R, C, L 

R, C, L = generate_underdamped_parameters()
print(f"R: {R} \nC: {C} \nL: {L}")
initial_conditions = [1.0, 0.0]  
t_span = (0, 50)  

# Plot the stream plot
plot_stream_system(system, R, C, L)

# Plot the solution graphs
plot_solution_graph(system, R, C, L, initial_conditions, t_span)
