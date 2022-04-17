from math import *
import math
import numpy as np
import matplotlib.pyplot as plt

class sila:
    def __init__(self):
        self.v = []
        self.x = []
        self.t = []
        self.a = []

    def set_initial_conditions(self, v, x, m, func):
        self.ti = 0
        self.dt = 0.01

        self.vi = v
        self.xi = x
        self.m = m
        self.func = func

    def reset(self):
        self.v = 0
        self.x = 0
        self.t = 0
        self.a = 0

    def move(self, t):
        for i in range(int(t/self.dt)):
            
            self.f = self.func(self.vi, self.xi, self.ti)
            self.ai = self.f/self.m

            self.vi = self.vi + self.ai * self.dt
            self.xi = self.xi + self.vi * self.dt
            self.ti = self.ti + self.dt
            
            self.a.append(self.ai)
            self.v.append(self.vi)
            self.x.append(self.xi)
            self.t.append(self.ti)
            
    def plot_trajectory(self):
        fig = plt.subplots(1,3,figsize = (13,4))
        plt.subplots_adjust(
        bottom = 0.1, right = 0.95, left = 0.1, top = 0.9)

        plt.subplot(1,3,1)
        plt.plot(self.t, self.x)
        plt.subplot(1,3,2)
        plt.plot(self.t, self.v)
        plt.subplot(1,3,3)
        plt.plot(self.t, self.a)
        plt.show()
