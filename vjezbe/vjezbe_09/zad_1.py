import math
import numpy as np
import matplotlib.pyplot as plt
from math import *
import bungeejumping as b

bj = b.BungeeJumping()
bj.set_initial_conditions(100,20,0,250,50,False)
bj.move(50)

plt.figure("Bungee jumping", figsize=(15, 10))
fig = plt.subplot()

plt.subplot(2,2,1)
plt.plot(bj.tl,bj.y)

plt.subplot(2,2,2)
plt.plot(bj.tl, bj.Euk)
plt.plot(bj.tl, bj.Ek)
plt.plot(bj.tl, bj.Ep)
plt.plot(bj.tl, bj.Eel)


bj = b.BungeeJumping()
bj.set_initial_conditions(100,20,0,250,50,True)    
bj.move(50)

plt.subplot(2,2,3)
plt.plot(bj.tl,bj.y)

plt.subplot(2,2,4)
plt.plot(bj.tl, bj.Euk,)
plt.plot(bj.tl, bj.Ek)
plt.plot(bj.tl, bj.Ep)
plt.plot(bj.tl, bj.Eel)
plt.show()