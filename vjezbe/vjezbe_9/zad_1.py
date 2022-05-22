import math
import numpy as np
import matplotlib.pyplot as plt
from math import *
import bungee as pct

p1 = pct.Bungee()
p1.set_initial_conditions(0, 30, 1, 1, 1, 6, 3, 10, 2)
xlista1, ylista1 = p1.euler()
plt.plot(xlista1, ylista1)