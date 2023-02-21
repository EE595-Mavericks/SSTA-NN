#ifndef SKEWED_RV_H
#define SKEWED_RV_H

#include "distribution.h"
#include "normal_rv.h"

class skewed_rv : public distribution{
public:
    skewed_rv(double mean, double variance, double skewness);

    ~skewed_rv();

    void get_parameter(double mean, double variance, double skewness);

    void get_moment(double location, double scale, double shape);

    double pdf(double x);

    double cdf(double x);
    
    void cal(double freq, ofstream *ofs);

    normal_rv helper_rv;

    double location;
    double scale;
    double shape;

};


#endif
