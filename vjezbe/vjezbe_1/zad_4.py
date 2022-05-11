def pravac(x1,y1,x2,y2):

    a = (int(y2)-int(y1))/(int(x2)-int(x1))
    b = int(y1)-a*int(x1)
    print("y =",a,"x +",b)

pravac(15,0,15,2)