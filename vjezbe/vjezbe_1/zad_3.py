x1 = input("Unesi x1:")
y1 = input("Unesi y1:")
x2 = input("Unesi x2:")
y2 = input("Unesi y2:")

if x1.isdigit() and y1.isdigit() and x2.isdigit() and y2.isdigit():
    a = (int(y2)-int(y1))/(int(x2)-int(x1))
    b = int(y1)-a*int(x1)
    print("y =",a,"x +",b)
else:
    print("ponovi")