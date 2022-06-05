import matplotlib.pyplot as plt
import numpy as np
import math

class Particle:
    
    def __init__(self):
        self.x = []
        self.y = []
        self.z = []

    def set_initial_conditions(self, E, B, v, q, m):
        self.q = q
        self.m = m
        self.E = E
        self.B = B
        self.v = v

        self.t = 0
        self.dt = 0.01
        self.a = np.array([0, 0, 0])
        x0 = 0
        y0 = 0
        z0 = 0

        self.x.append(x0)
        self.y.append(y0)
        self.z.append(z0)
    
    def reset(self):
        self.E = 0
        self.B = 0
        self.v = 0
        self.q = 0
        self.m = 0 

    def move(self):
        self.t = self.t + self.dt
        self.a = (self.q/self.m)*(self.E(self.t) + np.cross(self.v, self.B(self.t)))
        self.v = self.v + self.a*self.dt

        self.x.append(self.x[-1] + self.v[0]*self.dt)
        self.y.append(self.y[-1] + self.v[1]*self.dt)
        self.z.append(self.z[-1] + self.v[2]*self.dt)

    def range(self, tuk):
        while self.t <= tuk:
            self.move()
        return self.x, self.y, self.z




