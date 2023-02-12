#include "normal_rv.h"

class normal_rv {

public:
    normal_rv(double mean, double variance) : mean(mean), variance(variance) {
        stddev = sqrt(variance);
    }

    ~normal_rv() {}

    double pdf(double x) {
        double exponent = -0.5 * pow((x - mean) / stddev, 2);
        return (1.0 / (sqrt(2 * M_PI) * stddev)) * exp(exponent);
    }

    double cdf(double x) {
        return 0.5 * (1 + erf((x - mean) / (stddev * sqrt(2))));
    }

private:
    double mean;
    double variance;
    double stddev;

};
