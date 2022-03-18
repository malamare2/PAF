import numpy as np
import matplotlib.pyplot as plt
from math import *

F = 60
m = 4

def graf():
    
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

graf()