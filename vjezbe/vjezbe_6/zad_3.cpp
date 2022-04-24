#include <iostream>
#include <list>
#include <iterator>
#include <algorithm>


void polje(int lista[], int n)
{
    for(int i = 0; i < n; i++) 
    {
        std::cout << lista[i] << " ";
    }
    std::cout << std::endl;
}

int interval(int lista[], int n, int a, int b)
{
    std::cout << "interval " << a << "-" << b << ": ";
    for (int i = 0; i < n; i++)
    {
        if (lista[i]>= a && lista[i]<=b) 
        {
            std::cout << lista[i] << ", ";
        }
    }
    std::cout << std::endl;
}

void zamjena(int lista[], int i, int j)
{
    int t;
    t = lista[i];
    lista[i] = lista[j];
    lista[j] = t;
}

int main()
{
    int lista[10] = {1, 2, 3, 4, 5, 6, 7, 8, 0, -1};
    polje(lista, 10);

    interval(lista, 10, 0., 10.);
    std::cout << "lista: " << "";
    std::sort(std::begin(lista), std::end(lista));
    polje(lista, 10);

    std::reverse(std::begin(lista), std::end(lista));
    std::cout << "obrnuto: " << "";
    polje(lista, 10);

    zamjena(std::begin(lista), 3, 1);
    std::cout << "zamjena: " << "";
    polje(lista, 10);

    return 0;
}
