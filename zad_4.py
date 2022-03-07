def pravac():
    
    x1 = input("")
    y1 = input("")
    x2 = input("")
    y2 = input("")
    
    if x1.isdigit() and y1.isdigit() and x2.isdigit() and y2.isdigit():
        a = (int(y2)-int(y1))/(int(x2)-int(x1))
        b = int(y1)-a*int(x1)
        print("y =",a,"x +",b)
    else:
        print("ponovi")

pravac()