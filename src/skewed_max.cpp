#include "skewed_max.h"

using namespace std;

skewed_max::skewed_max(skewed_rv *x, skewed_rv *y) {
    this->X = x;
    this->Y = y;
}

double skewed_max::pdf(double z) {
    return X->cdf(z) * Y->pdf(z) + Y->cdf(z) * X->pdf(z);
}

double skewed_max::cdf(double z) {
    return 0;
}

void skewed_max::cal(double freq, ofstream *ofs) {

    double l_bound = max(X->mean - 10 * X->stddev, Y->mean - 10 * Y->stddev);
    double r_bound = max(X->mean + 10 * X->stddev, Y->mean + 10 * Y->stddev);

    double z = l_bound;
    double dz = (r_bound - l_bound) / freq;
    double one = 0.0;
    double square = 0.0;
    double cube = 0.0;
    // double total_prob = 0.0;

    for (int i = 0; i < freq; i++) {
        double tmp = pdf(z);
        if (i % 50 == 0) {
            if (ofs != nullptr) {
                *ofs << z << "," << tmp << endl;
            }
        }
        if (i == 0) {
            cout << tmp << " ";
        }
        if (i == freq - 1) {
            cout << tmp << " ";
        }
        one += z * tmp * dz;
        square += pow(z, 2) * tmp * dz;
        cube += pow(z, 3) * tmp * dz;
        // total_prob += tmp * dz;
        z += dz;
    }

    // cout << total_prob << " ";
    mean = one;
    variance = square - mean * mean;
    skewness = (cube - 3 * mean * variance - pow(mean, 3)) / pow(variance, 1.5);

}