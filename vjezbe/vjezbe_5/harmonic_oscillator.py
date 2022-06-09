import matplotlib.pyplot as plt
import math
from math import *

class HarmonicOscillator:
    def __init__(self):
        self.x = []
        self.v = []
        self.t = []
        self.a = []
    
    def set_initial_conditions(self, v0, x0, k, m, dt):
        self.v0 = v0
        self.x0 = x0
        self.k = k
        self.m = m
        self.dt = dt
        
        self.t.append(0)
        self.x.append(0)
        self.v.append(v0)
        self.a.append(0)

    def reset(self):
        self.v0 = 0
        self.theta = 0
        self.x0 = 0
        self.k = 0
        self.m = 0
        self.dt = 0

    def oscilate(self, t):   
        n = int(t/self.dt)
        for i in range(n):
            self.t.append(self.t[-1]+self.dt)
            self.a.append(-(self.k/self.m)*self.x[-1])
            self.v.append(self.v[-1]+self.a[-1]*self.dt)
            self.x.append(self.x[-1]+self.v[-1]*self.dt)
        return self.t, self.x 

    def tocnost(self):
        self.oscilate(2)
        return self.t, self.a, self.v, self.x

    def period(self, t):
        self.t, self.x = self.oscilate(t)
        c = max(self.x)
        d = self.x.index(c)  
        T = self.t[d]*4
        print(T)

    def analitickiperiod(self):
        T = 2*pi*sqrt(self.m/self.k)
        print(T)

   
