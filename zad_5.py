import matplotlib.pyplot as plt

def pravac():
    
    x1 = input("")
    y1 = input("")
    x2 = input("")
    y2 = input("")
    
    if x1.isdigit() and y1.isdigit() and x2.isdigit() and y2.isdigit():
        a = (int(y2)-int(y1))/(int(x2)-int(x1))
        b = int(y1)-a*int(x1)
        print("y =",a,"x +",b)

        c = "slika"
        d = "PDF"
        print("Želite li",c,"ili",d)
        f = input("")

        if f == c:
            plt.plot([x1,x2],[y1,y2])
            plt.show()
        elif f == d:
            plt.plot([x1,x2],[y1,y2])
            plt.savefig(input("ime: "), dpi='figure', format=None, metadata=None, bbox_inches=None, pad_inches=0.1, facecolor='auto', edgecolor='auto',backend=None)
        else:
            print("ponovi")

    else:
        print("ponovi")

pravac()

