#include <iostream>

// def pravac(x1,y1,x2,y2):

//     a = (int(y2)-int(y1))/(int(x2)-int(x1))
//     b = int(y1)-a*int(x1)
//     print("y =",a,"x +",b)

// pravac(5,6,4,7)


int pravac(int x1, int y1, int x2, int y2)

{
    int a = (y2 -y1) / (x2 - x1);
    int b = y1 - a*x1;
    std::cout << "y = "<< a << "x +" << b << std::endl;  
}

int main() {
    pravac(5,6,4,7);

    return 0;
}