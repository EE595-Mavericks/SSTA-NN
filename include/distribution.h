#include <cmath>
#include <iostream>

class distribution {
public:
    double mean;
    double variance;
    double stddev;
    double skewness;

    distribution();
    distribution(double mean, double variance);
    virtual double pdf(double x)=0;
    virtual double cdf(double x)=0;

};
