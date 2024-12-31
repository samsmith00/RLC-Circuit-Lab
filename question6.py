import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from numpy.linalg import eig
import math
import random

R = 2000 # ohms
C = 2 * 10**(-7) # farads
L = 1.5 # henrys
vt = 10 # volts

# [vc, i]
initial_condition = [10, 0]

t_span = (0,5)

def system(t, y, R, C, L, vt): 
    vc = y[0]
    i = y[1]

    # Equation 1
    dvc_dt = i/C

    # Equation 2
    di_dt = (vt -R*i - vc) / L

    return [dvc_dt, di_dt]


def calculate_eigenvalues(R, C, L): 
    A = np.array([[0, 1/C], [-1/L, -R/L]])
    eigenvals, eigenvects = eig(A)
    print(f"Eigenvalues: {eigenvals}")
    print(f"Eigenvectors: {eigenvects}")

calculate_eigenvalues(R, C, L)


sol = solve_ivp(system, t_span, initial_condition, args=(R, C, L, vt), dense_output=True)

# Evaluate the solution over the time points
t_vals = np.linspace(0, 5, 1000)
vc_vals = sol.sol(t_vals)[0]
i_vals = sol.sol(t_vals)[1]

# Plot Voltage and Current Over Time
plt.figure(figsize=(10, 6))

# Plot Voltage across the capacitor
plt.subplot(2, 1, 1)
plt.plot(t_vals, vc_vals, label="vc(t) (Voltage across Capacitor)", color='blue')
plt.axhline(y=vt, color='r', linestyle='--', label=f"Steady-state vc = {vt} V")
plt.xlabel("Time (s)")
plt.ylabel("Voltage (V)")
plt.legend()
plt.grid()

# Plot Current through the circuit
plt.subplot(2, 1, 2)
plt.plot(t_vals, i_vals, label="i(t) (Current through Circuit)", color='red')
plt.axhline(y=0, color='r', linestyle='--', label="Steady-state i = 0 A")
plt.xlabel("Time (s)")
plt.ylabel("Current (A)")
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()
