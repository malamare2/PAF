def pravac(x1,y1,x2,y2):

    if x1 != x2:
        a = (int(y2)-int(y1))/(int(x2)-int(x1))
        b = int(y1)-a*int(x1)
        print("y =",a,"x +",b)
    else:
        print("ponovi")

pravac(5,6,4,7)