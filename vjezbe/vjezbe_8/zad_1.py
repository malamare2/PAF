import Projectile as pct 
import matplotlib.pyplot as plt

p = pct.projectile()
p.set_initial_conditions(0, 0, 40, 10, 2, 1, 0.1, 1)
p.range1(0.01)

list_x, list_y = p.euler(0.01)
plt.plot(list_x, list_y)
plt.show()
