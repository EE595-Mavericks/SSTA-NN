#include "normal_max.h"
#include "skewed_max.h"

using namespace std;

int main(int argc, char *argv[]) {

    double muX = atof(argv[1]);
    double varX = atof(argv[2]);
    double muY = atof(argv[3]);
    double varY = atof(argv[4]);
    normal_rv x(muX, varX);
    normal_rv y(muY, varY);
    normal_max z(&x, &y);
    z.cal(10000);
    cout << z.mean << endl;
    cout << z.variance << endl;
    cout << z.skewness << endl;
}