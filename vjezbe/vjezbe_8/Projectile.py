import math
import numpy as np
import matplotlib.pyplot as plt
from math import *

class projectile:
    def __init__(self, x0, y0, theta, v0, m, r, c, a):
        self.x = []
        self.y = []
        self.t = []
        self.ay = []
        self.ax = []
        self.vx = []
        self.vy = []

        self.g = 9.81
        self.theta = theta
        self.v0 = v0
        self.y0 = y0
        self.x0 = x0

        self.m = m
        self.r = r
        self.c = c
        self.a = a


    def set_initial_conditions(self, x0, y0, theta, v0, m, r, c, a):
        theta = (theta/360)*2*np.pi
        self.theta = theta
        self.v0 = v0
        self.y0 = y0
        self.x0 = x0

        self.m = m
        self.r = r
        self.c = c
        self.a = a

      
        self.x.append(0)
        self.y.append(0)
        self.t.append(0)
        self.vx.append(v0*math.cos(self.theta))
        self.vy.append(v0*math.sin(self.theta))
        self.ax.append(0)
        self.ay.append(9.81)

    def reset(self):
        self.__init__(self.x0, self.y0, self.theta, self.v0, self.m, self.r, self.c, self.a)


    def move(self, dt):

        self.t.append(self.t[-1]+dt)

        self.ax.append(-((self.r * self.c *self.a)/(2*self.m))*(self.vx[-1])**2)
        self.ay.append(-self.g-((self.r * self.c * self.a)/(2*self.m))*(self.vy[-1])**2)

        self.vx.append(self.vx[-1]+self.ax[-1]*dt)
        self.vy.append(self.vy[-1]+self.ay[-1]*dt)

        self.x.append(self.x[-1]+self.vx[-1]*dt)
        self.y.append(self.y[-1]+self.vy[-1]*dt)

        print(self.vy)

    def range(self, dt):
        while (self.y[-1] >= 0):
            self.move(dt)
        print(self.x[-1])

    def plot_trajectory(self):
        plt.plot(self.x,self.y)
        plt.show()
















    



    




