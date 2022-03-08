import numpy as np
import matplotlib.pyplot as plt
from math import *

def kruznica():
    
    x = int(input("srediste x-os: "))
    y = int(input("srediste y-os: "))

    r = int(input("radius: "))

    z = int(input("tocka x-os: "))
    k = int(input("tocka y-os: "))

    kut = np.linspace( 0, 2 * np.pi)              #kružnica

    a = r * np.cos(kut) + x                     #parametri
    b = r * np.sin(kut) + y
 
    figure, axes = plt.subplots(1)
 
    axes.plot(a, b)
    axes.set_aspect(1)

    r2 = sqrt((x-z)*(x-z)+(y-k)*(y-k))        #udaljenost točke od središta kružnice(jednadžba kružnice)

    if r2 > r:
        print("Udaljenost tocke je",r2,"Nalazi se izvan kruznice")
    elif r2 == r:
        print("Udaljenost tocke je",r2,"Nalazi se na kruznici")
    else:
        print("Udaljenost tocke je",r2,"Nalazi se unutar")


    c = "slika"
    d = "PDF"
    print("Želite li",c,"ili",d)
    f = input("")

    if f == c:
        plt.scatter(x, y)
        plt.scatter(z, k)
        plt.show()
    elif f == d:
        plt.scatter(x, y)
        plt.scatter(z, k)
        plt.savefig(input("ime: "), dpi='figure', format=None, metadata=None, bbox_inches=None, pad_inches=0.1, facecolor='auto', edgecolor='auto',backend=None)
    else:
        print("ponovi")

kruznica()