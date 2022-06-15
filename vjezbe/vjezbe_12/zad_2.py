import numpy as np
import matplotlib.pyplot as plt
import Universe as universe
import matplotlib.animation as animation


au = 1.496 * 10**(11)
day = 60*60*24
year = 365.242*day

xe, ye = [], []
xs, ys = [], []
xmar,ymar = [],[]
xmer, ymer = [],[]
xv,yv = [], []

sunce = universe.Planet("Sunce", 1.989 * 10**30, np.array((0.,0.)), np.array((0.,0.)), "yellow")
merkur = universe.Planet("Merkur", 3.3 * 10**24, np.array((0., 0.466*au)), np.array((-47362., 0.)), "brown")
venera = universe.Planet("Venera", 4.8685*10**24, np.array((0.723*au, 0.)), np.array((0., 35020.)), "black")
zemlja = universe.Planet("Zemlja", 5.9742 * 10**24, np.array((float(-1. * au), 0.)), np.array((0., float(-29783))), "blue")
mars = universe.Planet("Mars",6.417*10**23, np.array((0., -1.666*au)), np.array((24007., 0.)), "red")

svemir = universe.Universe()
svemir.dodavanje(zemlja)
svemir.dodavanje(sunce)
svemir.dodavanje(merkur)
svemir.dodavanje(venera)
svemir.dodavanje(mars)

svemir.evolve(5)




fig = plt.figure(figsize=(10, 10)) 
ax = plt.axes(xlim=(-3e11, 3e11), ylim=(-3e11, 3e11))

line_sunce, = ax.plot([], [],'o',color=sunce.boja)
line_zemlja, = ax.plot([], [],'o',color=zemlja.boja)
line_merkur, = ax.plot([], [], 'o',color=merkur.boja)
line_venera, = ax.plot([], [], 'o',color=venera.boja)
line_mars, = ax.plot([], [], 'o',color=mars.boja)




def animate(i):
    xs.append(sunce.x[i])
    ys.append(sunce.y[i])

    xe.append(zemlja.x[i])
    ye.append(zemlja.y[i])
    
    xmer.append(merkur.x[i])
    ymer.append(merkur.y[i])
    
    xv.append(venera.x[i])
    yv.append(venera.y[i])
    
    xmar.append(mars.x[i])
    ymar.append(mars.y[i])

    line_sunce.set_data(xs[i],ys[i])
    line_zemlja.set_data(ye[i],xe[i])
    line_merkur.set_data(xmer[i],ymer[i])
    line_venera.set_data(xv[i],yv[i])
    line_mars.set_data(xmar[i],ymar[i])


plt.plot(sunce.x,sunce.y,color=sunce.boja, linewidth=5.0)
plt.plot(zemlja.x,zemlja.y,color=zemlja.boja)
plt.plot(mars.x,mars.y,color=mars.boja)
plt.plot(merkur.x,merkur.y,color=merkur.boja)
plt.plot(venera.x,venera.y,color=venera.boja)

anim = animation.FuncAnimation(fig, animate, interval=25)
plt.show()