import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from numpy.linalg import eig

HIGH = 10
LOW = 0.1


def system(t, y, R, C, L):
    vc = y[0]
    i = y[1]

   #Equation 1 
    dvc_dt = i / C 

    # Equation 2
    di_dt = -(R * i + vc) / L  
    
    return [dvc_dt, di_dt]  


def generate_stream_plot(system, R, C, L):
    # Create a grid in phase space
    vc = np.linspace(-7, 7, 20)
    i = np.linspace(-7, 7, 20)
    VC, I = np.meshgrid(vc, i)

    # Calculate Derivatives
    dVC_dt, dI_dt = np.zeros(VC.shape), np.zeros(I.shape)
    for row in range(VC.shape[0]): 
        for col in range(VC.shape[1]): 
            derivatives = system(0, [VC[row, col], I[row, col]], R, C, L)
            dVC_dt[row, col] = derivatives[0]
            dI_dt[row, col] = derivatives[1]
    
    # Get time and solutions
    solution = solve_ivp(system, t_span, initial_condition, args=(R, C, L), dense_output=True)
    t = np.linspace(t_span[0], t_span[1], 500)
    y = solution.sol(t)



    A = np.array([[0, 1/C], [-1/L, -R/C]])
    eigenvals, eigenvects = eig(A)
    print(f"Eigenvalues: {eigenvals}")



    # Plot streamline graph
    plt.figure(figsize=(8,6))
    plt.streamplot(VC, I, dVC_dt, dI_dt, color='blue', linewidth=1)
    plt.plot(y[0], y[1], color="red", label="Solution trajectory", linewidth=2)
    plt.title("Phase Space (Stream Plot)")
    plt.xlabel("Voltage across Capacitor ($v_C$)")
    plt.ylabel("Current ($i$)")
    plt.grid()
    plt.show()

    # Get the solution graph for system
def generate_solution_graph(system, R, L, C, t_span, initial_condition): 
    solution = solve_ivp(system, t_span, initial_condition, args=(R, C, L), dense_output=True)
    
    t = np.linspace(t_span[0], t_span[1], 500)
    y = solution.sol(t)

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

def generate_overdamped_parameters(): 
    C, L = get_random_parameters()

    R_min = np.sqrt(4 * L * C)
    R = np.random.uniform(R_min, HIGH)

    return [R, C, L]

R, C, L = generate_overdamped_parameters()
print(f"R: {R} \nC: {C} \nL: {L}")
initial_condition = [6.0, 0.0]  
t_span = (0, 50)  

generate_stream_plot(system, R, C, L)
generate_solution_graph(system, R, C, L, initial_condition, t_span)





