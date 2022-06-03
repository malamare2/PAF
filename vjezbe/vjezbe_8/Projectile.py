import math
import numpy as np
import matplotlib.pyplot as plt
from math import *

class projectile:
    def __init__(self):
        self.x = []
        self.y = []
        self.t = []
        self.ay = []
        self.ax = []
        self.vx = []
        self.vy = []

    def set_initial_conditions(self, x0, y0, theta, v0, m, r, c, a):
        self.g = 9.81
        self.dt = 0.01
        theta = (theta/360)*2*np.pi
        self.theta = theta
        self.v0 = v0
        self.y0 = y0
        self.x0 = x0
        self.m = m
        self.r = r  #gustoca
        self.c = c  #koef.trenja
        self.a = a   #povrsina tijela
      
        self.x.append(0)
        self.y.append(0)
        self.t.append(0)
        self.vx.append(v0*math.cos(self.theta))
        self.vy.append(v0*math.sin(self.theta))
        self.ax.append(0)
        self.ay.append(9.81)

    def reset(self):
        self.x0 = 0
        self.y0 = 0
        self.theta = 0
        self.v0 = 0
        self.m = 0
        self.r = 0
        self.c = 0
        self.a = 0

    def move(self, dt):

        self.t.append(self.t[-1]+dt)
        self.ax.append(-((self.r * self.c *self.a)/(2*self.m))*(self.vx[-1])**2)   #dodan otpor zraka
        self.ay.append(-self.g-((self.r * self.c * self.a)/(2*self.m))*(self.vy[-1])**2)
        self.vx.append(self.vx[-1]+self.ax[-1]*dt)
        self.vy.append(self.vy[-1]+self.ay[-1]*dt)
        self.x.append(self.x[-1]+self.vx[-1]*dt)
        self.y.append(self.y[-1]+self.vy[-1]*dt)

    def range1(self, dt):
        while (self.y[-1] >= 0):
            self.move(dt)
        print(self.x[-1])

    def euler(self, dt):
        self.range1(dt)
        return self.x, self.y

    def akcx(self, x, v, t):
        return -((self.r * self.c *self.a)/(2*self.m))*(self.vx[-1])**2

    def akcy(self, y, v, t):
        return - self.g - ((self.r*self.c*self.a)/(2*self.m))/(self.vy[-1])**2

    def runge_kutta(self):
        self.k1vx = self.akcx(self.x[-1], self.vx[-1], self.t[-1])* self.dt
        self.k1x = self.vx[-1] * self.dt
        self.k2vx = self.akcx((self.x[-1] + self.k1x/2), (self.vx[-1] + self.k1x/2), (self.t[-1] + self.dt/2))* self.dt
        self.k2x = (self.vx[-1] + (self.k1vx/2)) * self.dt
        self.k3vx = self.akcx((self.x[-1] + self.k2x/2), (self.vx[-1] + self.k2x/2), (self.t[-1] + self.dt/2))*self.dt
        self.k3x = (self.vx[-1] + (self.k2vx/2)) * self.dt
        self.k4vx = self.akcx((self.x[-1] + self.k3x), (self.vx[-1] + self.k3vx), (self.t[-1] + self.dt)) * self.dt
        self.k4x = self.vx[-1] * self.dt

        self.k1vy = self.akcy(self.y[-1], self.vy[-1], self.t[-1])* self.dt
        self.k1y = self.vy[-1] * self.dt
        self.k2vy = self.akcy((self.y[-1] + self.k1y/2), (self.vy[-1] + self.k1y/2), (self.t[-1] + self.dt/2))* self.dt
        self.k2y = (self.vy[-1] + (self.k1vy/2)) * self.dt
        self.k3vy = self.akcy((self.y[-1] + self.k2y/2), (self.vy[-1] + self.k2y/2), (self.t[-1] + self.dt/2))*self.dt
        self.k3y = (self.vy[-1] + (self.k2vy/2)) * self.dt
        self.k4vy = self.akcy((self.y[-1] + self.k3y), (self.vy[-1] + self.k3vy), (self.t[-1] + self.dt)) * self.dt
        self.k4y = self.vy[-1] * self.dt
        
        self.vx.append(self.vx[-1] + (1/6)*(self.k1vx + 2*self.k2vx + 2*self.k3vx + self.k4vx))
        self.x.append(self.x[-1] + (1/6)*(self.k1x + 2*self.k2x + 2*self.k3x + self.k4x))
        self.vy.append(self.vy[-1] + (1/6)*(self.k1vy + 2*self.k2vy + 2*self.k3vy + self.k4vy))
        self.y.append(self.y[-1] + (1/6)*(self.k1y + 2*self.k2y + 2*self.k3y + self.k4y))

    def range2(self):
        while self.y[-1] >= 0:
            self.runge_kutta()
        return self.x[-1]

    def runge(self):
        self.range2()
        return self.x, self.y

    




