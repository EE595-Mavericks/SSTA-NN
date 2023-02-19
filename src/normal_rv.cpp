#include "normal_rv.h"

//normal_rv::normal_rv(double mean, double variance) : distribution(mean, variance) {}

normal_rv::normal_rv(double mean, double variance) {
    this->mean = mean;
    this->variance = variance;
    this->stddev = sqrt(variance);
}

normal_rv::normal_rv() {}

normal_rv::~normal_rv() {}

double normal_rv::pdf(double x) {
    double exponent = -0.5 * pow((x - mean) / stddev, 2);
    return (1.0 / (sqrt(2 * M_PI) * stddev)) * exp(exponent);
}

double normal_rv::cdf(double x) {
    return 0.5 * (1 + erf((x - mean) / (stddev * sqrt(2))));
}
