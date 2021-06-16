import matplotlib.pyplot as plt
import numpy as np

t1 = 0
t2 = 50000

def g(x):
    return np.cos(2 * np.pi * 6 * x) + np.cos(2 * np.pi * 11 * x) + np.cos(2 * np.pi * 15 * x)

def centre_of_mass(f, t1, t2):
    real_part = 0
    imaginary_part = 0
    dt = 0.001

    n = int(t2-t1/dt)
    for t in range(0, n+1):
        real_part += g(t1 + (t * dt)) * np.cos(2 * np.pi * f * (t1 + (t * dt))) * dt
        imaginary_part += g(t1 + (t * dt)) * np.sin(2 * np.pi * f * (t1 + (t * dt))) * dt

    return np.sqrt((real_part)**2 + (imaginary_part)**2)


freq = np.linspace(0, 20, 1000)
com_real = centre_of_mass(freq, t1, t2)

time = np.linspace(t1, 20, 10000)

plt.plot(time, g(time), 'g', label='signal')
plt.plot(freq, com_real, 'k', label='fourier transform')
plt.xlabel('frequency')
plt.ylabel('sqrt(real part^2 + imaginary part^2)')
plt.title('cos(2pi 6 t) + cos(2pi  11 t) + cos(2pi 15 t) ; signal time = 5e10s')
plt.xticks([0, 5, 10, 15, 20, 6, 11, 15])
plt.legend()

plt.show()
