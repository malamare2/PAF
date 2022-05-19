import numpy as np
import matplotlib.pyplot as plt
from math import *


def jednoliko_gibanje(F,m):
    
    t = 10
    dt = 0.01

    a = []
    v = []
    x = []
    t = []

    v0 = 0
    x0 = 0
    t0 = 0
    akc = F/m

    for i in range(1000):
        t0 = t0 + dt
        v0 = v0 + akc*dt
        x0 = x0 + v0*dt

        a.append(akc)
        v.append(v0)
        x.append(x0)
        t.append(t0)
    

    fig = plt.subplots(1,3,figsize = (13,4))
    plt.subplots_adjust(
        bottom = 0.1, right = 0.95, left = 0.1, top = 0.9)
    plt.subplot(1,3,1)
    plt.title("a/t graf")
    plt.plot(t,a)
    plt.subplot(1,3,2)
    plt.title("v/t graf")
    plt.plot(t,v)
    plt.subplot(1,3,3)
    plt.title("x/t graf")
    plt.plot(t,x)
    plt.show()

