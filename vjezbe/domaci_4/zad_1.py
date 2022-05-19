import Projectile as pct
import matplotlib.pyplot as plt

p1 = pct.projectile()
p1.set_initial_conditions(0, 0, 40, 10, 2, 1, 0.1, 1, 1, 0, 0.5)
p1.tijelo()
xlista1, ylista1 = p1.runge()
plt.plot(xlista1, ylista1)

p2 = pct.projectile()
p2.set_initial_conditions(0, 0, 40, 10, 2, 1, 0.1, 1, 0, 1, 0.5)
p2.tijelo()
xlista2, ylista2 = p2.runge()
plt.plot(xlista2, ylista2)

plt.show()


