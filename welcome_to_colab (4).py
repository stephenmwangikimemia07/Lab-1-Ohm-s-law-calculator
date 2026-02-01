



import numpy as np
import matplotlib.pyplot as plt

R = 1000  # Ohms
C = 1e-6  # Farada
V = 5     # Volts

t = np.linspace(0, 0.01, 1000)
Vc = V * (1 - np.exp(-t / (R * C)))

plt.plot(t, Vc)
plt.xlabel("Time (s)")
plt.ylabel("Voltage (V)")
plt.title("RC Charging Curve")
plt.show()

Capacitor

"""Capacitor

"""

import numpy as np
import matplotlib.pyplot as plt

R = 2000  # New Resistance in Ohms
C = 2e-6  # New Capacitance in Farads
V = 5     # Volts (initial voltage)

t = np.linspace(0, 0.05, 1000) # Increased time range to better observe discharge with larger time constant
# Formula for a discharging capacitor
Vc = V * np.exp(-t / (R * C))

plt.plot(t, Vc)
plt.xlabel("Time (s)")
plt.ylabel("Voltage (V)")
plt.title(f"RC Discharging Curve (R={R} Ohms, C={C} Farads)")
plt.grid(True)
plt.show()

