x1 = int(input(""))
y1 = int(input(""))
x2 = int(input(""))
y2 = int(input(""))
    
def pravac():

    a = (y2-y1)/(x2-x1)
    b = y1-a*x1
    print("y =",a,"x +",b)

pravac()