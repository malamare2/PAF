import math
import numpy as np
import matplotlib.pyplot as plt
from math import *

class ProjectileDrop:
    def __init__(self):
        self.h = []
        self.vx = []
        self.vy = []
        self.t = []

        

    def set_initial_conditions(self, h0, v0x):
        v0y = 0

        self.h0 = h0
        self.v0x = v0x
        self.v0y = v0y
        self.t0 = 0

        self.h.append(self.h0)
        self.vx.append(self.v0x)
        self.vy.append(self.v0y)
        self.t.append(self.t0)

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

    def move(self,t, dt):
        g = 9.81
        n = int(t/dt)
        for i in range(n):
            self.x = []
            self.v0y = self.v0y - g*dt
            self.v0x = self.v0x - g*dt
            self.h0 = self.h0 + self.v0x*dt
            self.t0 = self.t0 + dt
            self.vy.append(self.v0y)
            self.vx.append(self.v0x)
            self.x.append(self.vx)

            self.h.append(self.h0)
            self.t.append(self.t0)
        
    def plot_trajectory(self):

        plt.figure("projectile")
        fig = plt.subplot()

        plt.subplot(2,1,1)
        plt.plot(self.t,self.vy)  # vy - t graf
        plt.subplot(2,1,2)
        plt.plot(self.vx,self.h) #x-y graf
        plt.show()

    def vrijeme_trajanja(self):
        print("Vrijeme trajanja padanja projektila",max(self.t))
    
    def meta(self, p, q, r):
        self.p = p
        self.q = q
        self.r = r

        r2 = self.p - self.q        

        if r2 > r:
            print("Udaljenost tocke je",r2,"Nalazi se izvan kruznice")
        elif r2 == r:
            print("Udaljenost tocke je",r2,"Nalazi se na kruznici")
        else:
            print("Udaljenost tocke je",r2,"Nalazi se unutar")
            

       
        







    