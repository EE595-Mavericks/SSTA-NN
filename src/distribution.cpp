#include "distribution.h"


distribution::distribution() {}

distribution::distribution(double mean, double variance) : mean(mean), variance(variance) {
    stddev = sqrt(variance);
}