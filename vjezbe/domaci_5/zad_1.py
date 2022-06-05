import particle as prt
import numpy as np
import matplotlib.pyplot as plt

def const(t):
    x = 0
    y = 0
    z = 0.1
    return np.array([x, y, z])

def prom(t):
    x = 0
    y = 0
    z = t/10
    return np.array([x, y, z])

p1 = prt.Particle()  #e- const
p2 = prt.Particle()  #e- prom
p3 = prt.Particle()  #p+ prom

p1.set_initial_conditions(const, const, np.array([0.1, 0.1, 0.1]), -1, 1)
p1.range(20)

p2.set_initial_conditions(prom, prom, np.array([0.1, 0.1, 0.1]), -1, 1)
p2.range(20)

p3.set_initial_conditions(const, prom, np.array([0.1, 0.1, 0.1]), 1, 1)
p3.range(20)

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot3D(p1.x, p1.y, p1.z)
ax.plot3D(p2.x, p2.y, p2.z)
ax.view_init(30, 30)
plt.show()

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot3D(p2.x, p2.y, p2.z)
ax.plot3D(p3.x, p3.y, p3.z)
ax.view_init(30, 30)
plt.show()

