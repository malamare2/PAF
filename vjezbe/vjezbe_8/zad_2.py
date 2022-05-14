import Projectile as pct
import matplotlib.pyplot as plt

p1 = pct.projectile()
p1.set_initial_conditions(0, 0, 50, 20, 2, 1, 0.01, 1)
x1_lista, y1_lista = p1.euler(0.01)

p2 = pct.projectile()
p2.set_initial_conditions(0, 0, 50, 20, 2, 1, 0.01, 1)
x2_lista, y2_lista = p2.runge()

plt.plot(x1_lista, y1_lista)
plt.plot(x2_lista, y2_lista)
plt.show()
