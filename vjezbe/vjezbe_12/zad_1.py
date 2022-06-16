import numpy as np
import matplotlib.pyplot as plt
import Universe as universe 

au = 1.496 * 10**(11)

sunce = universe.Planet("Sunce", 1.989 * 10**30, np.array((0.,0.)), np.array((0.,0.)), "yellow")
merkur = universe.Planet("Merkur", 3.3 * 10**24, np.array((0., 0.466*au)), np.array((-47362., 0.)), "brown")
venera = universe.Planet("Venera", 4.8685*10**24, np.array((0.723*au, 0.)), np.array((0., 35020.)), "orange")
zemlja = universe.Planet("Zemlja", 5.9742 * 10**24, np.array((float(-1. * au), 0.)), np.array((0., float(-29783))), "green")
mars = universe.Planet("Mars",6.417*10**23, np.array((0., -1.666*au)), np.array((24007., 0.)), "red")

ss = universe.Universe()
ss.dodavanje(zemlja)
ss.dodavanje(sunce)
ss.dodavanje(merkur)
ss.dodavanje(venera)
ss.dodavanje(mars)

ss.evolve(5)

plt.scatter(sunce.x, sunce.y, color = sunce.boja)
plt.plot(merkur.x, merkur.y, color = merkur.boja)
plt.scatter(merkur.x[-1], merkur.y[-1], color = merkur.boja)
plt.plot(venera.x, venera.y, color = venera.boja)
plt.scatter(venera.x[-1], venera.y[-1], color = venera.boja)
plt.plot(zemlja.x, zemlja.y, color = zemlja.boja)
plt.scatter(zemlja.x[-1], zemlja.y[-1], color = zemlja.boja)
plt.plot(mars.x, mars.y, color = mars.boja)
plt.scatter(mars.x[-1], mars.y[-1], color = mars.boja)

plt.show()