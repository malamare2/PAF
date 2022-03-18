x1 = input("")
y1 = input("")
x2 = input("")
y2 = input("")

if x1.isdigit() and y1.isdigit() and x2.isdigit() and y2.isdigit():
    
    x1 = int(x1)
    y1 = int(y1)
    x2 = int(x2)
    y2 = int(y2)

    a = (y2-y1)/(x2-x1)
    b = y1-a*x1
    print("y =",a,"x +",b)
else:
    print("ponovi")