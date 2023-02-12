#ifndef DISTRIBUTION_H
#define DISTRIBUTION_H

#include <cmath>
#include <iostream>
#include "float.h"

class distribution {
public:
    double mean;
    double variance;
    double stddev;
    double skewness;

    distribution();

    distribution(double mean, double variance);

    virtual double pdf(double x) = 0;

    virtual double cdf(double x) = 0;

};

#endif
