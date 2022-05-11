#include <iostream>
#include <Particle.h>

int main()
{
    Particle p1(70, 60, 0, 0);
    Particle p2(50, 35, 0, 0);

    std::cout << "Domet je " << p1.range() << std::endl;
    std::cout << "Vrijeme je " << p1.time() << std::endl;

    std::cout << "Domet je " << p2.range() << std::endl;
    std::cout << "Vrijeme je " << p2.time() << std::endl;
    
    return 0;
}