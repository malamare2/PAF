import numpy as np
import matplotlib.pyplot as plt
import math



y = []
theta = 60
dt = 0.01
v0 = 8

def max():
    y0 = 5
    v0y = v0*math.cos(theta)
    y0 = y0 + v0y*dt
    y.append(y0)
    y.sort()
    print(y[-1])
max()