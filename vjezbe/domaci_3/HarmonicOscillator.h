#include <iostream>
#include <vector>
#include <math.h>

class HarmonicOscillator
{
    private:
        double x0, v0, a, k, m, dt, t;
        void move();

    public:
        HarmonicOscillator(double x0, double v0, double k, double m, double dt);
        ~HarmonicOscillator();

        double pomak();
};