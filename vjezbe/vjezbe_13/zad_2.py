from gc import freeze
from tracemalloc import stop
import numpy as np
import matplotlib.pyplot as plt
import Universe as universe
import matplotlib.animation as animation

au = 1.496 * 10**(11)

# ime, masa, polozaj, v, boja
sunce = universe.Planet("Sunce", 1.989 * 10**30, np.array((0.,0.)), np.array((0.,0.)), "yellow")
merkur = universe.Planet("Merkur", 3.3 * 10**24, np.array((0., 0.466*au)), np.array((-47362., 0.)), "brown")
venera = universe.Planet("Venera", 4.8685*10**24, np.array((0.723*au, 0.)), np.array((0., 35020.)), "orange")
zemlja = universe.Planet("Zemlja", 5.9742 * 10**24, np.array((float(-1. * au), 0.)), np.array((0., float(-29783))), "green")
mars = universe.Planet("Mars",6.417*10**23, np.array((0., -1.666*au)), np.array((24007., 0.)), "red")
# comet = universe.Planet("Comet", 1e14, np.array([0.723*au, 2*au]), np.array([-15000, -20000]), "black")
comet = universe.Planet("Comet", 1e14, np.array([3*au, -2*au]), np.array([-25000, 5000]), "black")
# comet = universe.Planet("comet", 10**14, np.array((-4.*au, 1.7*au)), np.array((20000., 0.)), "black")

ss = universe.Universe()
ss.dodavanje(zemlja)
ss.dodavanje(sunce)
ss.dodavanje(merkur)
ss.dodavanje(venera)
ss.dodavanje(mars)
ss.dodavanje(comet)

ss.evolve(5)

fig = plt.figure(figsize=(10, 10)) 
ax = plt.axes(xlim = (-8e11, 8e11), ylim = (-8e11, 8e11))

xzemlja, yzemlja = [], []
xsunce, ysunce = [], []
xmars, ymars = [],[]
xmerkur, ymerkur = [],[]
xvenera, yvenera = [], []
xcomet, ycomet = [], []

line_sunce, = ax.plot([], [],'o',color = sunce.boja)
line_zemlja, = ax.plot([], [],'o',color = zemlja.boja)
line_merkur, = ax.plot([], [], 'o',color = merkur.boja)
line_venera, = ax.plot([], [], 'o',color = venera.boja)
line_mars, = ax.plot([], [], 'o',color = mars.boja)
line_comet, = ax.plot([], [], 'o',color = comet.boja)

def animate(i):
    xsunce.append(sunce.x[i])
    ysunce.append(sunce.y[i])
    line_sunce.set_data(xsunce[i],ysunce[i])

    xzemlja.append(zemlja.x[i])
    yzemlja.append(zemlja.y[i])
    line_zemlja.set_data(yzemlja[i],xzemlja[i])
    
    xmerkur.append(merkur.x[i])
    ymerkur.append(merkur.y[i])
    line_merkur.set_data(xmerkur[i],ymerkur[i])
    
    xvenera.append(venera.x[i])
    yvenera.append(venera.y[i])
    line_venera.set_data(xvenera[i],yvenera[i])
    
    xmars.append(mars.x[i])
    ymars.append(mars.y[i])
    line_mars.set_data(xmars[i],ymars[i])

    xcomet.append(comet.x[i])
    ycomet.append(comet.y[i])
    line_comet.set_data(xcomet[i], ycomet[i])

plt.plot(sunce.x, sunce.y, color=sunce.boja, linewidth=5.0)
plt.plot(zemlja.x, zemlja.y, color=zemlja.boja)
plt.plot(mars.x, mars.y, color=mars.boja)
plt.plot(merkur.x, merkur.y, color=merkur.boja)
plt.plot(venera.x, venera.y, color=venera.boja)
plt.plot(comet.x, comet.y, color=comet.boja)

anim = animation.FuncAnimation(fig, animate, interval=25)
plt.show()
