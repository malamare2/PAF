import Sunce_i_Zemlja as p
import matplotlib.pyplot as plt
import numpy as np

s_z = p.Z_S()
s_z.set_initial_conditions(np.array([1.466*10**(11), 0]), np.array([0.1, 0.1]), np.array([0, 28363]), np.array([0, 0]), np.array([0, 0]), np.array([0, 0]))
s_z.move()

plt.plot(s_z.xz, s_z.yz)
plt.plot(s_z.xs, s_z.ys)
plt.show()