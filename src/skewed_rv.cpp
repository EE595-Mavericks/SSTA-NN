#include "skewed_rv.h"

skewed_rv::skewed_rv(double mean, double variance, double skewness) {
    this->mean = mean;
    this->variance = variance;
    this->stddev = sqrt(variance);
    this->skewness = skewness;
}

skewed_rv::~skewed_rv() {

}

double skewed_rv::pdf(double x) {
    return 0;
}

double skewed_rv::cdf(double x) {
    return 0;
}
