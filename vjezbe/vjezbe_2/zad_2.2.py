import numpy as np
import matplotlib.pyplot as plt
from math import *

g = 9.81
vy = 5
dt = 0.01
n = 100
y = 0

V = []
Y = []
T = []

for i in range(n):
    vy = vy - g * dt
    V.append(vy)
    y = y + vy*dt
    Y.append(y)
    T.append(i*dt)

plt.plot(T,Y)
plt.show()