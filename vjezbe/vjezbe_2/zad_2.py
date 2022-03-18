import numpy as np
import matplotlib.pyplot as plt
import math

theta = 60

t = 10
dt = 0.01
g = 9.81
v0 = 5

v0x = v0*math.cos((theta/360)*2*np.pi)
v0y = v0*math.sin((theta/360)*2*np.pi)



y0 = 0
x0 = 0
t0 = 0

X = []
Y = []
T = []
V = []

for i in range(100):
    t0 = t0 + dt
    v0y = v0y-g*dt
    V.append(v0y)

    x0 = x0+v0x*dt
    X.append(x0)

    y0 = y0 + v0y*dt
    Y.append(y0)


    #x.append(x0)
    #y.append(y0)
    T.append(t0)

plt.subplot(1,3,1)
plt.plot(T,Y)
plt.subplot(1,3,2)
plt.plot(T,X)
plt.subplot(1,3,3)
plt.plot(X,Y)
plt.show()