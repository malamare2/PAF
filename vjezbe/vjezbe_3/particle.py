import math
import numpy as np
import matplotlib.pyplot as plt
from math import *


class Particle:
    def __init__ (self, x0, y0, theta, v0):
        self.x = []
        self.y = []
        self.vx = []
        self.vy = []
        self.ax = []
        self.ay = []
        self.t = []
        
        self.g = 9.81
        self.x0 = x0
        self.y0 = y0
        self.theta = theta
        self.v0 = v0
    
    def set_initial_conditions(self, theta, v0):
        self.vx.append(v0*math.cos((theta/360)*2*np.pi))
        self.vy.append(v0*math.sin((theta/360)*2*np.pi))
        self.x.append(0)
        self.y.append(0)
        self.t.append(0)
        self.ax.append(0)
        self.ay.append(9.81)

    def reset(self):
        self.vx = []
        self.vy = [] 
        self.x = []
        self.y = []

    def __move(self, dt):
        self.t.append(self.t[-1]+dt)
        self.vy.append(self.vy[-1]-self.g*dt)
        self.vx.append(self.vx[-1]+self.ax[-1]*dt)
        self.x.append(self.x[-1]+self.vx[-1]*dt)
        self.y.append(self.y[-1]+self.vy[-1]*dt)

    def range(self, dt):
        while (self.y[-1] >= 0):
            self.__move(dt)
        return (self.x[-1])

    def plot_trajectory(self):
        plt.plot(self.x, self.y)
        plt.show()

    def analiticki(self, theta):
        g = 9.81
        D = (self.v0**2)*sin(2*((theta/360)*2*np.pi))/g
        return D

    
    