from modul import sila 

def f1(v,x,t):
    return 100

p1 = sila()
p1.set_initial_conditions(30, 3, 3, f1)
p1.move(3)
p1.plot_trajectory()


def f2(v,x,t):
    k = 10
    return -k*x

p2 = sila()
p2.set_initial_conditions(30, 3, 3, f2)
p2.move(3)
p2.plot_trajectory()
