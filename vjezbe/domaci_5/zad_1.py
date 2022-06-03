import particle as prt
import numpy as np
import matplotlib.pyplot as plt


def B_const():
    B = np.array([0, 0, 0.1])
    return B

def B(t):
    B = np.array([0, 0, t/10])
    return B

def E_const():
    E = np.array([0, 0, 0])
    return E

def E(t):
    E = np.array([0, 0, t/10])
    return E

# elektron const
p1 = prt.Particle()
p1.set_initial_conditions(E_const, B_const, np.array([0.1, 0.1, 0.1]), -1, 1)
x1, y1, z1 = p1.range(10)


# elektron promj
p2 = prt.Particle()
p2.set_initial_conditions(E, B, np.array([0.1, 0.1, 0.1]), -1, 1)
x2, y2, z2 = p2.range(10)


# pozitron promj
p3 = prt.Particle()
p3.set_initial_conditions(E_const, B, np.array([0.1, 0.1, 0.1]), 1, 1)
x3, y3, z3 = p3.range(10)



fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot3D(x1, y1, z1, color="r", label="Konstantno")
ax.plot3D(x2, y2, z2, color="b", label="Promjenjivo")
ax.view_init(30, 30)
plt.legend()
plt.show()

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot3D(x2, y2, z2, color="r", label="Electron")
ax.plot3D(x3, y3, z3, color="b", label="Positron")
ax.view_init(30, 30)
plt.legend()
plt.show()