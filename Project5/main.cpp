#include <iostream>
#include <armadillo>
#include "planet.hpp"
#include <math.h>

using namespace std;
using namespace arma;


int main(){

    int n = 1e4;
    int yr = 1e3;
    double dt = yr/n;

    Planet earth;
    mat v(n,n, fill::zeros);
    mat r(n,n, fill::zeros);

    v(0,0) = M_PI;
    r(0,0) = 1;

    earth.initialize("Earth", 6e24, v[0], r[0]);

    for(int i=0; i<n; i++){
        earth.euler(i, dt );
    }


    return 0;
}
