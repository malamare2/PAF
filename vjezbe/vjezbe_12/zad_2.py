import numpy as np
import matplotlib.pyplot as plt
import Universe as universe
import matplotlib.animation as animation


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


fig = plt.figure(figsize=(7, 7))      #velicina slike (prozor)
ax = plt.axes(xlim=(-3e11, 3e11), ylim=(-3e11, 3e11)) 

xzemlja, yzemlja = [], []              #liste 
xsunce, ysunce = [], []
xmars, ymars = [],[]
xmerkur, ymerkur = [],[]
xvnera, yvenera = [], []

line_sunce, = ax.plot([], [],'o',color=sunce.boja)       #objekt linije koji se animira
line_zemlja, = ax.plot([], [],'o',color=zemlja.boja)
line_merkur, = ax.plot([], [], 'o',color=merkur.boja)
line_venera, = ax.plot([], [], 'o',color=venera.boja)
line_mars, = ax.plot([], [], 'o',color=mars.boja)

def animate(i):             #uzmemo jedan parametar i te crta pomak po x i y osi
    xsunce.append(sunce.x[i])
    ysunce.append(sunce.y[i])
    line_sunce.set_data(xsunce[i],ysunce[i])   #stvaranje osnovnog okvira na kojem se animacija odvija

    xzemlja.append(zemlja.x[i])
    yzemlja.append(zemlja.y[i])
    line_zemlja.set_data(yzemlja[i],xzemlja[i])

    xmerkur.append(merkur.x[i])
    ymerkur.append(merkur.y[i])
    line_merkur.set_data(xmerkur[i],ymerkur[i])

    xvnera.append(venera.x[i])
    yvenera.append(venera.y[i])
    line_venera.set_data(xvnera[i],yvenera[i])

    xmars.append(mars.x[i])
    ymars.append(mars.y[i])
    line_mars.set_data(xmars[i],ymars[i])

plt.plot(sunce.x,sunce.y,color=sunce.boja, linewidth=5.0)
plt.plot(zemlja.x,zemlja.y,color=zemlja.boja)
plt.plot(mars.x,mars.y,color=mars.boja)
plt.plot(merkur.x,merkur.y,color=merkur.boja)
plt.plot(venera.x,venera.y,color=venera.boja)

anim = animation.FuncAnimation(fig, animate, interval=1)
plt.show()


# https://jakevdp.github.io/blog/2012/08/18/matplotlib-animation-tutorial/