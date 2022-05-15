#include <iostream>
#include <vector>
#include <math.h>
#include <fstream>
#include <string>
#include <HarmonicOscillator.h>

using namespace std;

HarmonicOscillator::HarmonicOscillator(double x0, double v0, double k, double m, double dt)
{
    x0 = x0;
    v0 = v0;
    k = k;
    m = m;
    dt = dt;
    a = -k/m;
}

void HarmonicOscillator::move()
{
    a = -k/m * x0;
    v0 = v0 + a*dt;
    x0 = x0 + v0 * dt;
    t = t + dt;

}

double HarmonicOscillator::pomak()
{
    while (t <= 10)
    {
        move();
    }
    return 0;
}
