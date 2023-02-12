#include "distribution.h"

class skewed_max : distribution {

public:
    distribution *X;
    distribution *Y;

    skewed_max(distribution *x, distribution *y);

    double pdf(double z);

    double cdf(double z);

    void cal(double freq);

private:
    double phi(double x, double y);

    int I(double down, double up, double target);

    double joint_pdf(double x, double y);

};
