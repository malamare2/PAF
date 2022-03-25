import math
import numpy as np


class Particle:
    def __init__ (self):
        self.x = []
        self.y = []
        self.vx = []
        self.vy = []
        self.ax = []
        self.ay = []
        self.t = []
        self.dt = 0.1
    
    def set_initial_conditions(self, x0, y0, theta, v0):
        self.vx = v0*math.cos((theta/360)*2*np.pi)
        self.vy = v0*math.sin((theta/360)*2*np.pi)
        self.x = x0
        self.y = y0
        self.t = 0
        