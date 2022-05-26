import math
import numpy as np
import matplotlib.pyplot as plt
from math import *
import bungee as pct

# p1 = pct.Bungee()
# p1.set_initial_conditions(0, 30, 1, 1, 1, 6, 3, 10, 2)
# xlista1, ylista1 = p1.euler()
# plt.plot(xlista1, ylista1)

BJ=Bungee(100,20,0,250,50,False)
BJ.move(50)

plt.figure("Bungee jumping", figsize=(15, 10), dpi=80)
fig = plt.subplot()

plt.subplot(2,2,1)
plt.plot(BJ.t,BJ.h)
#plt.show()

plt.subplot(2,2,2)
plt.plot(BJ.t, BJ.Euk, label = "ukupna energija")
plt.plot(BJ.t, BJ.Ek, label = "kineticka energija")
plt.plot(BJ.t, BJ.Ep, label = "potencijalna energija")
plt.plot(BJ.t, BJ.Eel, label = "elasticna energija")
#plt.show()