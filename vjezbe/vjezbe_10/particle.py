import matplotlib.pyplot as plt
import numpy as np
import math

class Particle:
    def __init__(self):
        self.x = []
        self.y = []
        self.z = []
        self.t = []

    def set_initial_conditions(self, E, B, v, q, m):
        self.E = E
        self.B = B
        self.v = v
        self.q = q
        self.m = m

        self.a = np.array([0, 0, 0])
        self.dt = 0.01
        self.x0 = 0
        self.y0 = 0
        self.z0 = 0
        self.t0 = 0
        self.x.append(self.x0)
        self.y.append(self.y0)
        self.z.append(self.z0)
        self.t.append(self.t0)

    def reset(self):
        self.E = 0
        self.B = 0
        self.v = 0
        self.q = 0
        self.m = 0
        
    def move(self):
        self.t.append(self.t[-1] + self.dt)
        self.a = (self.q/self.m)*(self.E + np.cross(self.v, self.B))
        self.v = self.v + self.a*self.dt
        self.x.append(self.x[-1] + self.v[0]*self.dt)
        self.y.append(self.y[-1] + self.v[1]*self.dt)
        self.z.append(self.z[-1] + self.v[2]*self.dt)

    def akc(self, v):
        return self.q/self.m * (self.E +np.cross(v, self.B))

    def runge_kutta(self):
        self.t.append(self.t[-1] + self.dt)
        self.k1v = self.akc(self.v) *self.dt
        self.k1 = self.v*self.dt
        self.k2v = self.akc(self.v + self.k1v/2) * self.dt
        self.k2 = (self.v + self.k1v/2)*self.dt
        self.k3v = self.akc(self.v + self.k2v/2) * self.dt
        self.k3 = (self.v + self.k2v/2)*self.dt
        self.k4v = self.akc(self.v + self.k3v) * self.dt
        self.k4 = (self.v + self.k3v)*self.dt

        self.v = self.v + (1/6)*(self.k1v + 2*self.k2v + 2*self.k3v + self.k4v)

        self.x.append(self.x[-1] + (1/6)*(self.k1[0] + 2*self.k2[0] + 2*self.k3[0] + self.k4[0]))
        self.y.append(self.y[-1] + (1/6)*(self.k1[1] + 2*self.k2[1] + 2*self.k3[1] + self.k4[1]))
        self.z.append(self.z[-1] + (1/6)*(self.k1[2] + 2*self.k2[2] + 2*self.k3[2] + self.k4[2]))
    
    def range(self, t_uk):
        while self.t[-1] <= t_uk:
            self.move()
        return self.x, self.y, self.z

    def runge(self, t_uk):
        while self.t[-1] <= t_uk:
            self.runge_kutta()
        return self.x, self.y, self.z        