#include "normal_max.h"

normal_max::normal_max(normal_rv *x, normal_rv *y) {
    this->X = x;
    this->Y = y;
}

double normal_max::pdf(double z) {
    return X->cdf(z) * Y->pdf(z) + Y->cdf(z) * X->pdf(z);
}

double normal_max::cdf(double z) {
    return X->cdf(z) * Y->cdf(z);
}

void normal_max::cal(double start, double end, double freq) {
    double step = (end - start) / freq;
    double z = start;
    double z_square_mean = 0.0;
    double z_cube_mean = 0.0;

    for (int i = 0; i < freq; i++) {
        mean += z * pdf(z) * step;
        z_square_mean += pow(z, 2) * pdf(z) * step;
        z_cube_mean += pow(z, 3) * pdf(z) * step;
        z += step;
    }

    variance = z_square_mean - mean * mean;
    skewness = (z_cube_mean - 3 * mean * variance - pow(mean, 3)) / pow(variance, 1.5);
}