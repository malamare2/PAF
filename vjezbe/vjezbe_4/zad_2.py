import calculus as a
import math
import matplotlib.pyplot as plt

def f1(x):
    i = 5*x**3 - 2*x**2 + 2*x -3
    return i

def f1_int(x):
    integ = (5/4)*(x**4) - (2/3)*(x**3) + x**2 - 3*x
    return integ

dn = 100
gore = []
dole = []
trapez = []
korak = []
analiticki = []

for e in range(1, 50):
    n = e*dn
    korak.append(n)
    g = a.integ_pravokutnik(f1, 0, 9, n)[0]
    gore.append(g)
    d = a.integ_pravokutnik(f1, 0, 9, n)[1]
    dole.append(d)
    t = a.integ_traspez(f1, 0, 9, n)
    trapez.append(t)
    an = f1_int(9) - f1_int(0)
    analiticki.append(an)

s = [1]
plt.scatter(korak, gore, s, color = "blue")
plt.scatter(korak, dole, s, color = "red")
plt.scatter(korak, trapez, s, color = "green")
plt.plot(korak, analiticki, color = "yellow")
plt.show()