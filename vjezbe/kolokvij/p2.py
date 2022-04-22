class ProjectileDrop:
    def __init__(self):
        self.h = []
        self.vx = []
        self.vy = []
        self.t = []
        self.x  = []

        

    def set_initial_conditions(self, h0, v0x):
        v0y = 0
        x0 = 0

        self.h0 = h0
        self.v0x = v0x
        self.v0y = v0y
        self.t0 = 0
        self.x0 = x0

        self.h.append(self.h0)
        self.vx.append(self.v0x)
        self.vy.append(self.v0y)
        self.t.append(self.t0)
        self.x.append(self.x0)

        print("projektil je uspješno stvoren")
        print("na visini",self.h, "sa brzinom", self.vx)

    def reset(self):
        self.h = 0
        self.vx = 0
        self.vy = 0
        self.t = 0

    def novavisina(self, novi_h):
        self.novi_h = novi_h
        print("Nova visina iznosi: {:.2f}m".format(self.h0))

    def novabrzina(self,novi_v):
        self.novi_v = novi_v
        if self.novi_v > self.v0x:
            print("Nova brzina je veća i iznosi: {:.2f}m/s".format(self.novi_v))
        elif self.novi_v < self.v0x:
            print("Nova brzina je manja i iznosi: {:.2f}m/s".format(self.novi_v))
        else:
            print("Nova brzina je jednaka i iznosi: {:.2f}m/s".format(self.novi_v))

    def move(self, dt):
        g = 9.81
        for i in range(int(self.t/dt)):
            self.v0y = self.v0x - g*dt
            self.h0 = self.h0 + self.v0y*dt
            self.t0 = self.t0 + dt         
            self.x0 = self.x0 + self.v0x*dt   #pomicanje po x-osi

            self.vy.append(self.v0y)
            self.h.append(self.h0)
            self.t.append(self.t0)
            self.x.append(self.x0)
        return self.vy, self.h, self.t, self.x