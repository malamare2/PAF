import numpy as np
import matplotlib.pyplot as plt
import math
from math import *
def hitac(theta,v0):

    dt = 0.01
    g = 9.81

    v0x = v0*math.cos((theta/360)*2*np.pi)
    v0y = v0*math.sin((theta/360)*2*np.pi)

    y0 = 0
    x0 = 0

    X = [0]
    Y = [0]
    V = [0]

    for i in range(100):

        v0y = v0y-g*dt   #na brzinu na y-osi oduziman joj g i promjenu vremena i to apendam u praznu listu kako bi mi se mjenjalo za svaki mali dio
        V.append(v0y)

        x0 = x0+v0x*dt   #pomicanje po x-osi
        X.append(x0)

        y0 = y0 + v0y*dt  #pomicanje po y-osi
        Y.append(y0)


        if y0 < 0:    #ako visina padne ispod 0 prekida se i crta samo do tu
            break

    p = 7
    q = 0
    r = 0.5


    lista1 = []
    lista2 = []

    for j in X:
        c = p - j
        f = (p-c)*(p-c)
        lista1.append(f)

    for i in Y:
        k = q - i
        l = (q-k)*(q-k)
        lista2.append(l)
    
    lista = []
    for o in lista1:
        for s in lista2:
            d = sqrt(o + s)
            lista.append(d)


    lista.sort()   
    print(lista[0])
            


    kut = np.linspace( 0, 2 * np.pi)              #kružnica

    a = r * np.cos(kut) + p                     #parametri
    b = r * np.sin(kut) + q
 
    figure, axes = plt.subplots(1)
 
    axes.plot(a, b)
    axes.set_aspect(1)

    plt.plot(X,Y)
    plt.scatter(p, q)
    plt.show()


hitac(60,5)
