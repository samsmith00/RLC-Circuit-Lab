import numpy as np
from numpy.linalg import eig
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
import math
import random

R = 2000 # ohms
C = 2 * 10**(-7) # farads
L = 1.5 # henrys

# [vc, i]
initial_condition = [10, 0]

t_span = (0,5)

def system(t, y, R, C, L): 
    vc = y[0]
    i = y[1]

    # Equation 1
    dvc_dt = i/C

    # Equation 2
    di_dt = (-R*i - vc) / L

    return [dvc_dt, di_dt]


def solve_system(system, initial_condition, t_span, R, C, L): 
    solution = solve_ivp(system, t_span, initial_condition, args=(R, C, L), dense_output=True)
    

    return solution


def plot_phase_portrait(system, initial_condition, t_span, R, C, L): 
    vc = np.linspace(-1, 10, 20)
    i = np.linspace(-1, 1, 20)
    VC, I = np.meshgrid(vc, i)

    dVC_dt, dI_dt = np.zeros(VC.shape), np.zeros(I.shape)
    for row in range(VC.shape[0]): 
        for col in range(VC.shape[1]): 
            derivatives = system(0, [VC[row, col], I[row, col]], R, C, L)
            dVC_dt[row, col] = derivatives[0]
            dI_dt[row, col] = derivatives[1]
    
    solution = solve_system(system, initial_condition, t_span, R, C, L)
    t = np.linspace(t_span[0], t_span[1], 5000)
    y = solution.sol(t)
    print(solution.y[0])  # Voltage across the capacitor
    print(solution.y[1])  # Current in the circuit      

    plt.figure(figsize=(8, 6))
    plt.streamplot(VC, I, dVC_dt, dI_dt, color='blue', linewidth=1)
    plt.plot(y[0], y[1], color='red', label="Solution trajectory", linewidth=2)
    plt.title("Phase Portrait")
    plt.xlabel("Voltage across Capacitor ($v_C$)")
    plt.ylabel("Current ($i$)")
    plt.grid()
    plt.show()


def generate_solution_graph(system, initial_condition, t_span, R, C, L):

    solution = solve_system(system, initial_condition, t_span, R, C, L)
    t = np.linspace(t_span[0], t_span[1], 500000)
    y = solution.sol(t)

    plt.figure(figsize=(10, 6))
    plt.plot(t, y[0], label="$v_C(t)$ (Voltage across Capacitor)")
    plt.plot(t, y[1], label="$i(t)$ (Current through Circuit)")
    plt.title("Solution Graphs")
    plt.xlabel("Time ($t$)")
    plt.ylabel("$v_C(t)$, $i(t)$")
    plt.axhline(0, color="black", linewidth=1, linestyle="--")
    plt.axvline(0, color="black", linewidth=1, linestyle="--")
    plt.legend()
    plt.grid()
    plt.show()


def calculate_eigenvalues(R, C, L): 
    A = np.array([[0, 1/C], [-1/L, -R/L]])
    eigenvals, eigenvects = eig(A)
    print(f"Eigenvalues: {eigenvals}")
    print(f"Eigenvectors: {eigenvects}")

calculate_eigenvalues(R, C, L)

#plot_phase_portrait(system, initial_condition, t_span, R, C, L)
#generate_solution_graph(system, initial_condition, t_span, R, C, L)






