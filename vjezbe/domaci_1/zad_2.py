import math
import numpy as np
import matplotlib.pyplot as plt
from math import *
import particle as prt

#1.graf

dometlista = []
kutlista = []

p1 = prt.Particle(60, 30, 20, 50, 0.01)

for kut in range(180):
    p1.set_initial_conditions(60, 30, kut, 50, 0.01)
    
    kut = (kut/360)*2*np.pi
    kutlista.append(kut)

    domet = p1.range()
    dometlista.append(domet)

plt.plot(kutlista,dometlista)
plt.show()

#2.graf

dometlista = []
brzinalista = []

p1 = prt.Particle(60, 30, 20, 50, 0.01)

for brzina in range(100):
    p1.set_initial_conditions(60, 30, 20, brzina, 0.01)

    brzinalista.append(brzina)

    domet = p1.range()
    dometlista.append(domet)

plt.plot(brzinalista, dometlista)
plt.show()

#3.graf

trajanjelista = []
kutlista = []

p1 = prt.Particle(60, 30, 20, 50, 0.01)

for kut in range(180):
    p1.set_initial_conditions(60, 30, kut, 50, 0.01)

    kut = (kut/360)*2*np.pi
    kutlista.append(kut)

    trajanje = p1.total_time()
    trajanjelista.append(trajanje)

plt.plot(kutlista ,trajanjelista)
plt.show()

#4.graf

trajanjelista = []
brzinalista = []

p1 = prt.Particle(60, 30, 20, 50, 0.01)

for brzina in range(100):
    p1.set_initial_conditions(60, 30, 20, brzina, 0.01)

    brzinalista.append(brzina)

    trajanje = p1.total_time()
    trajanjelista.append(trajanje)

plt.plot(brzinalista ,trajanjelista)
plt.show()


