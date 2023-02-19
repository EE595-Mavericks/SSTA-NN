#include "normal_max.h"
#include "skewed_max.h"
#include <iomanip>

using namespace std;

int main(int argc, char *argv[]) {

    double muX = atof(argv[1]);
    double varX = atof(argv[2]);
    double skewX = atof(argv[3]);
    double muY = atof(argv[4]);
    double varY = atof(argv[5]);
    double skewY = atof(argv[6]);

    skewed_rv x(muX, varX, skewX);
    skewed_rv y(muY, varY, skewY);

    x.cal(10000);
    // skewed_max z(&x, &y);

    // z.cal(10000);

    // cout << setprecision(5) << fixed;
    // cout << x.mean << " " << x.variance << " " << x.skewness << endl;
    // cout << y.mean << " " << y.variance << " " << y.skewness << endl;
    // cout << z.mean << " " << z.variance << " " << z.skewness << endl;

}