#include "skewed_rv.h"

using namespace std;

skewed_rv::skewed_rv(double mean, double variance, double skewness) {
    this->mean = mean;
    this->variance = variance;
    this->stddev = sqrt(variance);
    this->skewness = skewness;
    get_parameter(mean, variance, skewness);

    // purpose: use pdf and cdf of standard normal distribution to calculate pdf of this skew normal rv
    helper_rv = normal_rv(0, 1);
}

skewed_rv::~skewed_rv() {

}

void skewed_rv::get_parameter(double mean, double variance, double skewness) {
    double delta_square = (M_PI / 2) * pow(fabs(skewness), 2.0 / 3.0) /
                          (pow(fabs(skewness), 2.0 / 3.0) + pow((4 - M_PI) / 2, 2.0 / 3.0));
    double delta = pow(delta_square, 0.5);
    delta = skewness >= 0 ? delta : -delta;
    this->shape = pow(delta_square / (1 - delta_square), 0.5);
    this->shape = skewness >= 0 ? this->shape : -this->shape;
    this->scale = pow(variance / (1 - 2 * delta_square / M_PI), 0.5);
    this->location = mean - scale * delta * pow(2 / M_PI, 0.5);
}

double skewed_rv::pdf(double x) {
    double trans = (x - location) / scale;
    return (2 / scale) * helper_rv.pdf(trans) * helper_rv.cdf(shape * trans);
}

double skewed_rv::cdf(double x) {
    int freq = 10000;

    double l_bound = mean - 10 * stddev;
    double r_bound = mean + 10 * stddev;
    double dt = (r_bound - l_bound) / freq;
    double t = l_bound;
    double cdf = 0.0;

    while (t < x) {
        cdf += pdf(t) * dt;
        t += dt;
    }

    return cdf;
}

void skewed_rv::cal(double freq, ofstream *ofs) {

    double l_bound = mean - 10 * stddev;
    double r_bound = mean + 10 * stddev;

    double z = l_bound;
    double dz = (r_bound - l_bound) / freq;
    double one = 0.0;
    double square = 0.0;
    double cube = 0.0;

    for (int i = 0; i < freq; i++) {
        if (i % 50 == 0) {
            double tmp = pdf(z);
            if (ofs != nullptr) {
                *ofs << z << "," << tmp << endl;
            }
        }
        one += z * pdf(z) * dz;
        square += pow(z, 2) * pdf(z) * dz;
        cube += pow(z, 3) * pdf(z) * dz;
        z += dz;
    }

    double m = one;
    double v = square - m * m;
    double s = (cube - 3 * m * v - pow(m, 3)) / pow(v, 1.5);

    // std::cout << m << " " << v << " " << s << std::endl;

}

void skewed_rv::get_moment(double location, double scale, double shape) {

    double delta = shape / pow(1 + shape * shape, 0.5);
    double delta_square = pow(delta, 2);
    this->mean = location + scale * delta * pow(2 / M_PI, 0.5);
    this->variance = pow(scale, 2) * (1 - 2 * delta_square / M_PI);
    this->skewness = (4 - M_PI) / 2 *
                     pow(delta * pow(2 / M_PI, 0.5), 3) /
                     pow(1 - 2 * delta_square / M_PI, 1.5);
}

