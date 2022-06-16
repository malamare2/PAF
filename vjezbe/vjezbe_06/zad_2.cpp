#include <math.h>
#include <iostream>
using namespace std;

int kruznica(int x, int y, int r, int p, int q)
{
    int d;
    d = sqrt(((x-p), 2.0) + ((y - q), 2.0));
    if (d > r)
    {
        cout << "Tocka je izvan kruznice." << endl;
    }
    if (d == r)
    {
        cout << " Tocka je na kruznici." << endl;
    }
    if (d < r)
    {
        cout << "Tocka je u kruznici." << endl;
    }
}

int main()
{
    kruznica(3, 3, 4, 1, 1);
    return 0;
}

