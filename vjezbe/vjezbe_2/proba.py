import numpy as np
import matplotlib.pyplot as plt
import math
from math import *


#kosi hitac

def kosi(theta,v0):

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


        if y0 < 0:    #ako visina padne ispod 0 prekida se i crta samo do tu
            break

    plt.title("x/y graf")
    plt.plot(X,Y)
    plt.show()


#udaljenost mete od kosog hitca

    def meta(p,q,r):
       
        lista1 = []
        lista2 = []


        for j in X:                            #za svaki element na x-osi 
            if j <= p:                         #ako se razlikuje od središta mete
                c = p - j
                lista1.append(c)
            else:                      #oduzmemo prvu kordinatu za izračunavanje udaljenosti (x2 - x1)
                c = j - p              #spreme se svi rezultati u listu
                lista1.append(c)                     

        for i in Y:                            #za svaki element na y-osi
            if i <= q:                         #ako se razlikuje od stredišta mete
                k = q - i 
                lista2.append(k)
            else:
                k = i - q                     #oduzmemo drugu kordinatu za izračunavanje udaljenosti (y2 - y1)
                lista2.append(k)               #spreme se svi rezultati u listu

        lista = []                             
        for o in lista1:                       #za svaki element u x-osi listi
            for s in lista2:                   #za svaki elementr u y_osi listi
                d = sqrt((o*o + s*s) - r)        #formula za udaljenost dviju točaka i oduzmemo radijus mete da odredimo najkraću udaljenost od mete(a ne od centra)
            lista.append(d)                    #dobiveni rezultati se spreme u listu koja se sortira i izvuce se najmanja udaljenost
            lista.sort()



        if o > r and o - r > r and s > r and s - r > r or lista[0] > r:
            print("najbliza udaljenost od mete je:",lista[0])
        elif o < r and r - o > r and s < r and r - s > r or lista[0] > r:
            print("najbliza udaljenost od mete je:",lista[0])
        else:
            print("meta je pogođena", lista[0])


        kut = np.linspace( 0, 2 * np.pi)              #kružnica

        a = r * np.cos(kut) + p                     #parametri
        b = r * np.sin(kut) + q
 
        figure, axes = plt.subplots(1)
 
        axes.plot(a, b)
        axes.set_aspect(1)

        plt.scatter(p, q)
        plt.plot(X,Y)
        plt.show()

    meta(1,1,0.5)

# max visina, domet, brzina

    def hmax(Y):         #max visina koju tijelo postigne
        Y.sort()         
        print("maksimalna visina:",Y[-1])
    hmax(Y)

    def dom(X):
        print("domet:",X[-1])  #domet tijela(tocka na koju je palo tijelo)
    dom(X)

    def vmax(V):
        V.sort()
        print("maksimalna brzina:",V[-1])    #maksimalna brzina koju tijelo postigne
    vmax(V)