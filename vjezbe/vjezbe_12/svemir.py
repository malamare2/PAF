import Sunce_planeti as p
import matplotlib.pyplot as plt
import numpy as np

s_z = p.Z_S()
s_z.set_initial_conditions(np.array([1.466*10**(11), 0]), np.array([0.1, 0.1]), np.array([4.600101*10**(10), 0]), np.array([0, 28363]), np.array([0, 0]), np.array([0, 47362]), np.array([0, 0]), np.array([0, 0]), np.array([0, 0]))
s_z.move()

plt.plot(s_z.xz, s_z.yz)
plt.plot(s_z.xs, s_z.ys)
plt.plot(s_z.xm, s_z.ym)
plt.plot(s_z.xs2, s_z.ys2)
plt.show()