import particle as prt
import matplotlib.pyplot as plt

# odstupanje u gibanju

p1 = prt.Particle(0, 0, 40, 10)
p1.set_initial_conditions(40, 10)

odstupanje = abs(((p1.analiticki(40) - p1.range(0.01)))/p1.analiticki(40))*100
print("odstupanje je:",odstupanje)
print(p1.range(0.1))

# graf greške

p1 = prt.Particle(0, 0, 60, 10)
p = []
pogreska = []
    
for i in range(1000):
    p1.set_initial_conditions(60, 10)
    promjena = i * 0.001
    p.append(promjena)
    pogreska1 = abs(((p1.analiticki(60) - p1.range(promjena)))/p1.analiticki(40))*100
    pogreska.append(pogreska1)
    p1.reset()


plt.plot(p, pogreska)
plt.show()
