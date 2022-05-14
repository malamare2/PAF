import Projectile as pct
import matplotlib.pyplot as plt
import numpy as np


c_lista = list(np.linspace(0, 3, 30))
range_l=[]
p1 = pct.projectile()

for c in c_lista:
    p1.c = c
    p1.set_initial_conditions(0, 0, 29.65, 50, 0.1, 1.2, c, 0.01)
    range_l.append(p1.range2())

plt.plot(c_lista, range_l)
plt.show()



m_lista = list(np.linspace(0.01, 10, 50))
range_l=[]
p2 = pct.projectile()

for m in m_lista:
    p2.m = m
    p2.set_initial_conditions(0, 0, 40, 60, m, 1.2, 0.1, 0.01)
    range_l.append(p2.range2())

plt.plot(m_lista, range_l)
plt.show()

