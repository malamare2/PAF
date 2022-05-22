class Bungee:
    def __init__(self):
        self.y = []
        self.t = []
        self.akc = []
        self.v = []

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
        self.v.append(0)
        self.akc.append(self.g)
        
        self.Ep.append(self.m*(-self.akc)*(self.y[-1]))
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

    def move(self):

        self.t.append(self.t[-1]+self.dt)
        self.v.append(self.v[-1]+self.akc[-1]*self.dt)
        self.y.append(self.y[-1]+self.v[-1]*self.dt)
