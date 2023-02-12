#include <cmath>
#include <iostream>

class distribution {
public:
    double mean;
    double variance;
    double stddev;

    distribution();
    distribution(double mean, double variance);
    virtual void pdf()=0;
    virtual void cdf()=0;

};
