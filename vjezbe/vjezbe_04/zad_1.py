import calculus as a        # importa gotove metode
import math
import matplotlib.pyplot as plt

def kubna(x):
    return x**3 - 3*x**2 +5

def trigonometrijska(x):
    return math.sin(x)


lista1, lista2 = a.derivacija(kubna, 0, 4, 0.01, 0)
lista3, lista4 = a.derivacija(kubna, 0, 4, 0.1, 0)
lista5 = []

for x in lista2:
    lista5.append(3*x**2 - 6*x)   

s = [2]
plt.scatter(lista2, lista1, s, color = "green")
plt.scatter(lista4, lista3, s, color = "blue")
plt.plot(lista2, lista5, color = "orange")

plt.pause(2)
plt.show

lista1, lista2 = a.derivacija(trigonometrijska, 0, 4, 0.01, 1)
lista3, lista4 = a.derivacija(trigonometrijska, 0, 4, 0.1, 1)

lista5 = []
for x in lista2:
    lista5.append(math.cos(x))


plt.clf()

s = [2]
plt.scatter(lista2, lista1, s, color = "green")
plt.scatter(lista4, lista3, s, color = "blue")
plt.plot(lista2, lista5, color = "orange")

plt.pause(2)
plt.show