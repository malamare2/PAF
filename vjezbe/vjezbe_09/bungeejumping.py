import numpy as np
import math
import matplotlib.pyplot as plt

class BungeeJumping:
    def __init__(self):
        self.y = [] 
        self.tl = [] 
        self.Ep = [] 
        self.Ek = [] 
        self.Eel = []  
        self.Euk = [] 
    
    def set_initial_conditions(self,m,k,v0,h0,l,r=1,c=1,al=1,otpor = True):
        self.m=m 
        self.k=k
        self.v0 = v0
        self.l=l
        self.h0=h0
        self.r=r
        self.c=c
        self.al=al
        self.otpor = otpor
        self.h=h0

        self.dt = 0.001
        self.g = 9.81
        self.U=self.m * self.g * self.h

        self.v0=0 
        self.t=0 
        self.K=0 
        self.Ee=0
        
        self.y.append(self.h)
        self.tl.append(self.t)
        self.Ep.append(self.U)
        self.Ek.append(self.K)
        self.Eel.append(self.Ee)
        self.Euk.append(self.U + self.K + self.Ee)
    
    def reset(self):
        self.m = 0
        self.k = 0
        self.v0 = 0
        self.h0 = 0
        self.l = 0
        self.r = 0
        self.c = 0
        self.al = 0
        self.dt = 0
        self.otpor = 0

    def el(self):          #jeli palo sktroz ili jos pada(elasticna sila)
        dh = self.h0 - self.l - self.h
        self.dh = dh
        if dh > 0:
            self.a_el = (self.k/self.m)*dh
        else: 
            self.a_el = 0
        return self.al

    def otpor_z(self):     #imali ili ne otpor zraka
        if self.otpor:
            self.a_otpor = -(abs(self.v0)*self.v0*self.r*self.c*self.al)/(2*self.m)
        else:
            self.a_otpor = 0
        return self.a_otpor

    def akceleracija(self):   
        self.el()
        self.otpor_z() 
        
        a = -self.g + self.a_el + self.a_otpor
        return a

    def energija(self):
        if self.dh > 0:
            self.Ee = 0.5*self.k*self.dh**2
        self.U=self.m * 9.81 * self.h
        self.K = 0.5*self.m*(self.v0)**2
        self.E = self.U + self.K + self.Ee

    def __move(self):
        self.a = self.akceleracija()
        self.v0 += self.a*self.dt
        self.h += self.v0*self.dt
        self.t += self.dt
        self.energija()

    def move(self,t):
        while self.t < t:
            self.__move()
            self.y.append(self.h)
            self.tl.append(self.t)
            self.Eel.append(self.Ee)
            self.Ek.append(self.K)
            self.Ep.append(self.U)
            self.Euk.append(self.E)
    