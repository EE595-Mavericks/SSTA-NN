#ifndef SKEWED_MAX_H
#define SKEWED_MAX_H

#include "skewed_rv.h"

class skewed_max : public distribution {

public:
    skewed_rv *X;
    skewed_rv *Y;
    double location;
    double scale;
    double shape;
    normal_rv helper_rv;

    skewed_max(skewed_rv *x, skewed_rv *y);

    double pdf(double z);

    double cdf(double z);

    void cal(double freq, ofstream *ofs);

};

#endif
