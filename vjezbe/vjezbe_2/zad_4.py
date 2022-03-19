import numpy as np
import matplotlib.pyplot as plt
import math


def kosi_hitac(theta,v0):

    t = 10
    dt = 0.01
    g = 9.81


    v0x = v0*math.cos((theta/360)*2*np.pi)
    v0y = v0*math.sin((theta/360)*2*np.pi)

    y0 = 0
    x0 = 0
    t0 = 0

    X = [0]
    Y = [0]
    T = [0]
    V = [0]

    for i in range(100):
        t0 = t0 + dt   #na staro vrijeme dodajem novo vrijeme

        v0y = v0y-g*dt   #na brzinu na y-osi oduziman joj g i promjenu vremena i to apendam u praznu listu kako bi mi se mjenjalo za svaki mali dio
        V.append(v0y)

        x0 = x0+v0x*dt   #pomicanje po x-osi
        X.append(x0)

        y0 = y0 + v0y*dt  #pomicanje po y-osi
        Y.append(y0)
        T.append(t0)

        if y0 < 0:
            break

    plt.title("x/y graf")
    plt.plot(X,Y)
    plt.show()

kosi_hitac(60,5)