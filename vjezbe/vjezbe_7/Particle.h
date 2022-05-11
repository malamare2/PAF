#include <iostream>

class Particle
{
    private:

        double t, x, y, vx, vy;
        double dt = 0.001;
        double g = -9.81;

        void move();
    
    public: 

        Particle(double v0, double theta, double x0, double y0);

        double range();
        double time();

};