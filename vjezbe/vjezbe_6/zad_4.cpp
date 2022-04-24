#include <iostream>

int jednadzba(int a1, int b1, int c1, int a2, int b2, int c2)
{
    int x; 
    x = (b1*c2 - b2*c1)/(b1*a2 - a1*b2);

    int y;
    y = (a1*c2 - a2*c1) / (a1*b2 - a2*b1);

    std::cout << "x = " << x << std::endl;
    std::cout << "y = " << y << std::endl;
}

int main()
{
    jednadzba(4, 2, 5, 7, 3, 4);
    return 0;
}