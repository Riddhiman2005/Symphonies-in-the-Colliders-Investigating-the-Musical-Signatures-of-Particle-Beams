import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def lorentz_force(q, v, B):
  
  # Lorentz force equation
  
    return q * np.cross(v, B)

def particle_motion(y, t, q, m, B_func):
  
    # Differential equation describing the particle's motion
    
    r, v = y[:3], y[3:]
    B = B_func(t)  
    
    # Evaluate the magnetic field at time t
    
    dvdt = lorentz_force(q, v, B) / m
    drdt = v
    return np.concatenate((drdt, dvdt))

def magnetic_field(t):
    
    # Function defining the time-varying magnetic field B(t)
    
    # Replace this with your own magnetic field expression
    
    B0 = 1.0  
    # Magnitude of the magnetic field
    
    omega = 2.0  
    
    # Angular frequency of the field variation
    
    Bx = B0 * np.cos(omega * t)
    By = B0 * np.sin(omega * t)
    Bz = 0.0
    return np.array([Bx, By, Bz])

# Get input from the user

q = float(input("Please enter the charge of the particle: "))
m = float(input("Please enter the mass of the particle: "))

# Initial conditions

r0 = np.array([0.0, 0.0, 0.0])  # Initial position
v0 = np.array([1.0, 1.0, 0.0])  # Initial velocity
y0 = np.concatenate((r0, v0))

# Time span
t_start = 0.0
t_end = 10.0
dt = 0.01
t = np.arange(t_start, t_end, dt)

# Solve the differential equation
sol = odeint(particle_motion, y0, t, args=(q, m, magnetic_field))

# Extract position components from the solution
x, y, z = sol[:, 0], sol[:, 1], sol[:, 2]

# Plotting the trajectory

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()
