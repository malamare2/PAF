import particle as prt
import numpy as np
import matplotlib.pyplot as plt

p1 = prt.Particle()
p1.set_initial_conditions(np.array([0., 0., 0.]), np.array([0., 0., 1.]), np.array([0.1, 0.1, 0.1]), -1, 1)
x1, y1, z1 = p1.range(10)
p2 = prt.Particle()
p2.set_initial_conditions(np.array([0., 0., 0.]), np.array([0., 0., 1.]), np.array([0.1, 0.1, 0.1]), -1, 1)
x2, y2, z2 = p2.runge(10)

ax = plt.axes(projection='3d')
ax.plot3D(x1, y1, z1)
ax.plot3D(x2, y2, z2)
ax.view_init(30, 30)
plt.show()