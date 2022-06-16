import numpy as np
import matplotlib.pyplot as plt
import math

class Planet:

    def __init__(self, ime, masa, polozaj, v, boja):
        self.ime = ime
        self.masa = masa
        self.polozaj = polozaj
        self.v = v
        self.boja = boja
        
        self.x = []
        self.y = []

        self.x.append(polozaj[0])
        self.y.append(polozaj[1])

class Universe:

    def __init__(self):
        self.planeti = []
        self.G = 6.67408*10**(-11)
        self.dt = 3600*24
        self.trajanje = 0

    def dodavanje(self, planet):
        self.planeti.append(planet)

    def move(self):
        for p1 in self.planeti:
            p1.a = np.array([0, 0])
            for p2 in self.planeti:
                if p1 != p2:

                    d = (p1.polozaj - p2.polozaj)**2
                    p1.a = p1.a - self.G*(p2.masa / (math.sqrt(d[0] + d[1]))**3 )*(p1.polozaj - p2.polozaj)

            p1.v = p1.v + p1.a * self.dt
            p1.polozaj = p1.polozaj + p1.v * self.dt
            p1.x.append(p1.polozaj[0])
            p1.y.append(p1.polozaj[1])

        self.trajanje = self.trajanje + self.dt

    def evolve(self, t):
        godina = 365.242 * 24 * 60 * 60
        while self.trajanje < godina*t:
            self.move()