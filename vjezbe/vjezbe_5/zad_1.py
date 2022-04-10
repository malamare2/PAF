import harmonic_oscillator as h
import matplotlib.pyplot as plt
import math
from math import *

h1 = h.HarmonicOscillator()
h1.set_initial_conditions(3, 100, 0, 5, 0.01)
h1.oscilate(3)
h1.graf()


h1.oscilate(3)
fig, axes = plt.subplots(1, 3, figsize=(13, 4))

h1.set_initial_conditions(3, 10, 0, 5, 0.001)
axes[0].scatter(h1.t, h1.x)

h1.set_initial_conditions(3, 10, 0, 5, 0.01)
axes[1].scatter(h1.t, h1.x)

h1.set_initial_conditions(3, 10, 0, 5, 0.05)
axes[2].scatter(h1.t, h1.x)

plt.show()


#ne radi

# fig, axes = plt.subplots(1, 3, figsize=(13, 4))

# h2 = h.HarmonicOscillator()
# h2.oscilate(3)
# h2.set_initial_conditions(3, 10, 0, 5, 0.001)
# axes[0].plot(h2.t, h2.x)

# h3 = h.HarmonicOscillator()
# h3.oscilate(3)
# h3.set_initial_conditions(3, 10, 0, 5, 0.01)
# axes[1].plot(h3.t, h3.x)

# h4 = h.HarmonicOscillator()
# h4.oscilate(3)
# h4.set_initial_conditions(3, 10, 0, 5, 0.05)
# axes[2].plot(h4.t, h4.x)

# plt.show()