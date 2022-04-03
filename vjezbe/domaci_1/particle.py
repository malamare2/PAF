import math
import numpy as np
import matplotlib.pyplot as plt
from math import *


class Particle:
    def __init__ (self, x0, y0, theta, v0, dt):
        self.X = []
        self.Y = []
        self.V = []
        self.ax = []
        self.ay = []
        self.t = []
        
        self.dt = dt
        self.g = 9.81
        self.x0 = x0
        self.y0 = y0
        self.theta = theta
        self.v0 = v0
    
    def set_initial_conditions(self, x0, y0, theta, v0, dt):
        self.x = x0
        self.y = y0
        self.v0 = v0
        self.dt = dt

        self.ax.append(0)
        self.ay.append(9.81)
        self.t.append(0)
        self.X.append(x0)
        self.Y.append(y0)

        self.vx = self.v0*math.cos((theta/360)*2*np.pi)
        self.vy = self.v0*math.sin((theta/360)*2*np.pi)

    def reset(self):
        self.vx = 0
        self.vy = 0 
        self.x = []
        self.y = []

    def __move(self):
        self.t.append(self.t[-1]+self.dt)

        self.vy = self.vy - self.g * self.dt   #brzina na y-osi
        self.vx = self.vx - self.g * self.dt   #brzina na x-osi
        
        self.x = self.x + self.vx * self.dt    #pomicanje po x-osi
        self.X.append(self.x)

        self.y = self.y + self.vy * self.dt     #pomicanje po y-osi
        self.Y.append(self.y)

        self.v = sqrt(self.vx**2 + self.vy**2)   #ukupna brzin za x i y osi
        self.V.append(self.v)

    def range(self):
        while self.y >= 0:
            self.__move()
        return max(self.X)

    def plot_trajectory(self):
        plt.plot(self.X, self.Y)
        plt.show()

    def analiticki(self, theta):
        g = 9.81
        D = (self.v0**2)*sin(2*((theta/360)*2*np.pi))/g
        return D


    def total_time(self):
        self.__move()
        t_uk = self.t[-1] + self.dt
        return t_uk

    def max_speed(self):
        return max(self.V)


    def velocity_to_hit_target(self, p, q, r, theta):
        vmin = 0
        vmax = 100
        self.vx = self.v0*math.cos((theta/360)*2*np.pi)
        self.vy = self.v0*math.sin((theta/360)*2*np.pi)

        for self.v0 in range(vmin, vmax):
            self.__move()
            d = sqrt((p-self.x)**2 + (q-self.y)**2)

            if d <= r:
                break
            
        return "pocetna brzina" ,self.v0 ,"m/s"


    def angle_to_hit_target(self, p, q, r, theta):
        
        self.vx = self.v0*math.cos((theta/360)*2*np.pi)
        self.vy = self.v0*math.sin((theta/360)*2*np.pi)
        
        for kut in range(89):
            self.__move()
            d = sqrt((p-self.x)**2 + (q-self.y)**2)
            theta = kut/360 *2*np.pi

            if d <= r:
                break
        
        return "kut je", kut
            



                








       