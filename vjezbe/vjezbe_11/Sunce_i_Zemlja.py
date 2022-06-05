import matplotlib.pyplot as plt
import numpy as np
import math

class Z_S:
    
    def __init__(self): 
        self.xz = []
        self.yz = []
        self.xs = []
        self.ys = []
        self.t = []
    
    def set_initial_conditions(self, rz, rs, vz, vs, az, asu):   #za sunce (2.) i zemlju (1.)
        self.rz = rz
        self.rs = rs
        self.vz = vz
        self.vs = vs
        self.az = az
        self.asu = asu

        self.mz = 5.9742*((10)**24)
        self.ms = 1.989*((10)**30)
    
        self.G = 6.67408*10**(-11)
        self.tuk = 365.242*24*3600
        self.dt = 100
        xz = 1.486*10**(11)
        yz = 0
        xs = 0
        ys = 0
        t = 0
        
        self.xz.append(xz)
        self.yz.append(yz)
        self.xs.append(xs)
        self.ys.append(ys)
        self.t.append(t)

    def reset(self):
        self.rz = 0
        self.rs = 0
        self.vz = 0
        self.vs = 0
        self.az = 0
        self.asu = 0

    def zemlja(self):
        d1 = (self.rz - self.rs)**2
        self.n1 = math.sqrt(d1[0] + d1[1])

    def sunce(self):
        d2 = (self.rs - self.rz)**2
        self.n2 = math.sqrt(d2[0] + d2[1])
    
    def move(self):
        while self.t[-1] <= self.tuk:
            self.zemlja()
            self.sunce()
            self.t.append(self.t[-1] + self.dt)
        
            self.a1 = -self.G*(self.ms / self.n1**3 )*(self.rz - self.rs)
            self.a2 = -self.G*(self.mz / self.n2**3 )*(self.rs - self.rz)

            self.vz = self.vz + self.az*self.dt
            self.vs = self.vs + self.asu*self.dt

            self.rz = self.rz + self.vz*self.dt
            self.rs = self.rs + self.vs*self.dt

            self.xz.append(self.rz[0])
            self.yz.append(self.rz[1])
            self.xs.append(self.rs[0])
            self.ys.append(self.rs[1])
        return self.xz, self.yz, self.xs, self.ys

        