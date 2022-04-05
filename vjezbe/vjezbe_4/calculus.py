import numpy as np
import math
import matplotlib.pyplot as plt
from math import *


def dthreepoint(func, x, h):
    d=(func(x+h)-func(x-h))/(2*h)    #formula za derivaciju 3.point
    return(d)

def dtwopoint(func, x, h):
    d = (func(x+h)-func(x))/h        #formula za derivaciju 2.point
    return(d)


#2.metoda
def derivacija(func, a, b, h, metoda):

    lista1 = list(np.arange(a, b, h))    #lista tocaka u rasponu
    lista2 = []

    for x in lista1:

        if metoda == 3:          #zadana velicina koraka derivacije
            deriv = dthreepoint(func, x, h)   
        else:
            deriv = dtwopoint(func, x, h)
        y = deriv

        lista2.append(y)        # lista iznosa derivacija tocaka koje vraca
    return(lista2, lista1)


def integ_pravokutnik(f, a, b, n):

    dx = (b-a)/n
    sum_b = 0        # donja međa
    sum_a = 0        # gornja međa

    x = a
    y = a+dx

    for i in range(n):
        sum_a = sum_a + f(x)*dx
        sum_b = sum_b + f(y)*dx

        x = x+dx
        y = y+dx

    return (sum_a, sum_b)


def integ_traspez(f, a, b, n):

    dx = (b-a)/n
    suma = 0
 
    for i in range(n):
        suma = suma + f(a)
        a = a + dx
        trapez = suma * dx + ((f(b) + f(a))/2)*dx
    return(trapez)