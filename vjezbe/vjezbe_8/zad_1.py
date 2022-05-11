import Projectile as pct 
#x0, y0, theta, v0, m, r, c, a
pct = pct.projectile(0, 0, 40, 10, 2, 1, 0.1, 1)
pct.set_initial_conditions(0, 0, 40, 10, 2, 1, 0.1, 1)
pct.range(0.01)
pct.plot_trajectory()
