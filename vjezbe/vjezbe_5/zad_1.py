import harmonic_oscillator as ho
import matplotlib.pyplot as plt
import math


ho1 = ho.HarmonicOscillator()
ho2 = ho.HarmonicOscillator()
ho1.set_initial_conditions(3, 0, 5, 15, 0.1, 0.01)
ho2.set_initial_conditions(3, 0, 5, 15, 0.1, 0.05)
t1, a1, v1, x1 = ho1.tocnost()
t2, a2, v2, x2 = ho2.tocnost()

fig = plt.subplots(1, 3, figsize=(13, 4))

plt.subplot(1,3,1)
plt.plot(t1, x1)
plt.scatter(t2, x2)

plt.subplot(1,3,2)
plt.plot(t1, v1)
plt.scatter(t2, v2)

plt.subplot(1,3,3)
plt.plot(t1, a1)
plt.scatter(t2, a2)

plt.show()


