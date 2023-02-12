#ifndef NORMAL_RV_H
#define NORMAL_RV_H

#include "distribution.h"


class normal_rv : public distribution {

public:
    normal_rv(double mean, double variance);

    ~normal_rv();

    double pdf(double x);

    double cdf(double x);

};

#endif