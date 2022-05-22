import matplotlib.pyplot as plt
import math as m

class HarmonicOscillator:
    def __init__(self):
        self.x = []
        self.v = []
        self.t = []
        self.a = []

    def set_initial_conditions(self, m, k, x0, v0, dt):
        self.k = k
        self.m = m
        self.x0 = x0
        self.v0 = v0
        self.dt = dt
        
        self.x.append(x0)
        self.v.append(v0)
        self.t.append(0)
        self.a.append(0)

    def reset(self):
        self.__init__(self.m, self.k, self.x0, self.v0)
        
    def oscilate(self, t):
        n = int(t/self.dt)
        for i in range(n):
            self.t.append(self.t[-1]+self.dt)
            self.a.append((self.k/self.m)*self.x[-1])
            self.v.append(self.v[-1]+self.a[-1]*self.dt)
            self.x.append(self.x[-1]-self.v[-1]*self.dt)
        return self.a, self.t, self.v, self.x 

    def period(self, t):
        self.t, self.x = self.oscilate(t)
        c = max(self.x)
        d = self.x.index(c)
        e = self.t[d]
        T = e*4
        return(T)

    def analitickiperiod(self):
        T = 2*m.pi*m.sqrt(self.m/self.k)
        return(T)

    def graf(self):
        fig, axes = plt.subplots(1, 3, figsize=(13, 4))
        axes[0].plot(self.t, self.x)
        axes[1].plot(self.t, self.v)
        axes[2].plot(self.t, self.a)
        plt.show()


    








        
        