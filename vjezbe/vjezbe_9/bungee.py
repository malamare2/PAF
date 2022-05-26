class Bungee:
    def __init__(self):
        self.y = [] #visina
        self.t = []

        self.Ep = []
        self.Ek = []
        self.Eel = []
        self.Euk = []

    def set_initial_conditions(self, y0, v0, r, c, a, h, k, l, m):
        self.g = 9.81
        self.dt = 0.01
        self.y0 = y0
        self.v0 = v0
        self.r = r
        self.c = c
        self.a = a
        self.h = h
        self.k = k
        self.l = l
        self.m = m

        self.y.append(h)
        self.t.append(0)
        
        self.Ep.append(self.m * 9.81 * self.h)
        self.Ek.append(0)
        self.Eel.append(0)
        self.Euk.append(self.Ep[-1] + self.Ek[-1] + self.Eel[-1])

    def reset(self):
        self.x0 = 0
        self.y0 = 0
        self.v0 = 0
        self.r = 0
        self.c = 0
        self.a = 0
        self.h = 0

    def akcy(self, y, v, t):
        return - self.g - ((self.r*self.c*self.a)/(2*self.m))/(self.vy[-1])**2

    def energija(self):
        self.Ep = self.m * 9.81 * self.h
        self.Ek = 0.5*self.m*(self.v0)**2
        self.Euk = self.Ep + self.Ek + self.Eel
        return self.Euk

        

    def __move(self):
        self.a = self.akcy()

        self.v0 += self.a*self.dt
        self.h += self.v0*self.dt
        self.t += self.dt
        
        self.energija()

    def move(self,t):
        while self.t < t:
            self.__move()
            self.h.append(self.h)
            self.t.append(self.t)
            self.Eel.append(self.Eel)
            self.Ek.append(self.Ek)
            self.Ep.append(self.Ep)
            self.Euk.append(self.Euk)

