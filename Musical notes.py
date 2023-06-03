
import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import write

# Particle properties
electron_charge = 1.6e-19      # Charge of electron (C)
proton_charge = 1.6e-19        # Charge of proton (C)
neutron_charge = 0             # Charge of neutron (C)
electron_mass = 9.1e-31        # Mass of electron (kg)
proton_mass = 1.67e-27         # Mass of proton (kg)
neutron_mass = 1.67e-27        # Mass of neutron (kg)

# Magnetic field properties
B0 = 1.0         # Strength of magnetic field at z=0 (T)
dBdz_factor = 1e-4      # Scaling factor for the rate of change of magnetic field with respect to z (T/m)
z_threshold = 1.0   # Z-coordinate threshold for hitting the surface (m)

# Time properties
t0 = 0           # Initial time (s)
tmax = 1e-7      # Maximum simulation time (s)
dt = 1e-12       # Time step (s)
N = int(tmax/dt) # Number of time steps

# Function to calculate the magnetic field at a given z-coordinate based on particle properties
def magnetic_field_z(z, particle_charge, particle_mass):
    dBdz = dBdz_factor * particle_charge / particle_mass
    return B0 + dBdz * z

# Function to calculate the Lorentz force
def lorentz(q, v, B):
    return q * np.cross(v, B)

# Function to calculate the acceleration of the particle
def acceleration(q, v, B, m):
    return lorentz(q, v, B) / m

# Initialize arrays to store the particle's position and velocity
x = np.zeros(N)
y = np.zeros(N)
z = np.zeros(N)
vx = np.zeros(N)
vy = np.zeros(N)
vz = np.zeros(N)

# Set the initial position and velocity of the particle
x[0] = 0
y[0] = 0
z[0] = 0
vx[0] = 1e6
vy[0] = 0
vz[0] = 0

# Use the fourth-order Runge-Kutta method to solve the equations of motion
for i in range(1, N):
    t = t0 + i * dt
    if z[i-1] < z_threshold:
        Bz = magnetic_field_z(z[i-1], electron_charge, electron_mass)
        charge = electron_charge
        mass = electron_mass
    else:
        Bz = magnetic_field_z(z[i-1], proton_charge, proton_mass)
        charge = proton_charge
        mass = proton_mass

    k1v = acceleration(charge, np.array([vx[i-1], vy[i-1], vz[i-1]]), np.array([0, 0, Bz]), mass) * dt
    k1x = np.array([vx[i-1], vy[i-1], vz[i-1]]) * dt
    k2v = acceleration(charge, np.array([vx[i-1] + k1v[0]/2, vy[i-1] + k1v[1]/2, vz[i-1] + k1v[2]/2]), np.array([0, 0, Bz]), mass) * dt
    k2x = np.array([vx[i-1] + k1v[0]/2, vy[i-1] + k1v[1]/2, vz[i-1] + k1v[2]/2]) * dt
    k3v = acceleration(charge, np.array([vx[i-1] + k2v[0]/2, vy[i-1] + k2v[1]/2, vz[i-1] + k2v[2]/2]), np.array([0, 0, Bz]), mass) * dt
    k3x = np.array([vx[i-1] + k2v[0]/2, vy[i-1] + k2v[1]/2, vz[i-1] + k2v[2]/2]) * dt
    k4v = acceleration(charge, np.array([vx[i-1] + k3v[0], vy[i-1] + k3v[1], vz[i-1] + k3v[2]]), np.array([0, 0, Bz]), mass) * dt
    k4x = np.array([vx[i-1] + k3v[0], vy[i-1] + k3v[1], vz[i-1] + k3v[2]]) * dt

    vx[i] = vx[i-1] + (k1v[0] + 2*k2v[0] + 2*k3v[0] + k4v[0]) / 6
    vy[i] = vy[i-1] + (k1v[1] + 2*k2v[1] + 2*k3v[1] + k4v[1]) / 6
    vz[i] = vz[i-1] + (k1v[2] + 2*k2v[2] + 2*k3v[2] + k4v[2]) / 6

    x[i] = x[i-1] + (k1x[0] + 2*k2x[0] + 2*k3x[0] + k4x[0]) / 6
    y[i] = y[i-1] + (k1x[1] + 2*k2x[1] + 2*k3x[1] + k4x[1]) / 6
    z[i] = z[i-1] + (k1x[2] + 2*k2x[2] + 2*k3x[2] + k4x[2]) / 6

# Detect particles and generate musical notes
notes = []
for i in range(N):
    if z[i] >= z_threshold:
        if charge == electron_charge:
            notes.append('C')
        elif charge == proton_charge:
            notes.append('A')
        elif charge == neutron_charge:
            notes.append('G')

# Plot the trajectory
plt.figure()
plt.plot(x, z)
plt.xlabel('x (m)')
plt.ylabel('z (m)')
plt.title('Trajectory of Charged Particles')
plt.grid(True)
plt.show()

# Save the musical notes as a WAV file
sampling_rate = 44100
duration = tmax
t = np.linspace(0, duration, int(sampling_rate * duration))
frequencies = {'C': 261.63, 'A': 440.00, 'G': 392.00}
samples = np.zeros(len(t))
for note in notes:
    frequency = frequencies[note]
    samples += np.sin(2 * np.pi * frequency * t)
samples /= len(notes)
scaled_samples = np.int16(samples * 32767)
write('particle_notes.wav', sampling_rate, scaled_samples)
