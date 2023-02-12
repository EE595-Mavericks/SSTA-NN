#ifndef EE595_PROJ_SKEWED_RV_H
#define EE595_PROJ_SKEWED_RV_H

#include "distribution.h"

class skewed_rv : public distribution{
public:
    skewed_rv(double mean, double variance, double skewness);

    ~skewed_rv();

    double pdf(double x);

    double cdf(double x);
};


#endif //EE595_PROJ_SKEWED_RV_H
