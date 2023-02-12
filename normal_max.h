#include "normal_rv.h"


class normal_max : distribution {

public:
    normal_rv *X;
    normal_rv *Y;

    normal_max(normal_rv *x, normal_rv *y);

    double pdf(double z);

    double cdf(double z);

    void cal(double start, double end, double freq);

};


