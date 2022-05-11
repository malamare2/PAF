#include <Particle.h>
#include <math.h>
#include <cmath>
#include <iostream>

Particle::Particle(double v0, double theta, double x0, double y0)
{
    t = 0;
    x = x0; 
    y = y0;
    vy = v0 * sin(theta);
    vx = v0 * cos(theta);
}

void Particle::move()
{
    vx = vx + 0;
    vy = vy + g * dt;
    x = x + vx * dt;
    y = y + vy * dt;
    t = t + dt;

}

double Particle::range()
{
    while (y >= 0)
    {
        move();
    }
    return x;
}

double Particle::time()
{
    while (y >= 0)
    {
        move();
    }
    return t;
}

