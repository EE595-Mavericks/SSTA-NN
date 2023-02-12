#include "skewed_max.h"

using namespace std;

skewed_max::skewed_max(skewed_rv *x, skewed_rv *y) {
    this->X = x;
    this->Y = y;
}

double skewed_max::pdf(double z) {

    return 0;
}

double skewed_max::cdf(double z) {

    return 0;
}

double skewed_max::phi(double x, double y) {
    double res = exp(-(pow(x, 2) + pow(y, 2)) / 2);
    return res;
}

int skewed_max::I(double down, double up, double target) {
    return target < up && target > down ? 1 : 0;
}

double skewed_max::joint_pdf(double x, double y) {
    double tau = M_PI / 2 * (X->skewness + 1 / X->skewness) * (Y->skewness + 1 / Y->skewness);
    double sigma_x_l = X->stddev / X->skewness;
    double sigma_y_l = Y->stddev / Y->skewness;
    double sigma_x_r = X->stddev * X->skewness;
    double sigma_y_r = Y->stddev * Y->skewness;

    double res = 1 / (tau * X->stddev * Y->stddev) * (
            phi((x - X->mean) / sigma_x_l, (y - Y->mean) / sigma_y_l) *
            I(-DBL_MAX, X->mean, x) *
            I(-DBL_MAX, Y->mean, y) +
            phi((x - X->mean) / sigma_x_l, (y - Y->mean) / sigma_y_r) *
            I(-DBL_MAX, X->mean, x) *
            I(Y->mean, DBL_MAX, y) +
            phi((x - X->mean) / sigma_x_r, (y - Y->mean) / sigma_y_l) *
            I(X->mean, DBL_MAX, x) *
            I(-DBL_MAX, Y->mean, y) +
            phi((x - X->mean) / sigma_x_r, (y - Y->mean) / sigma_y_r) *
            I(X->mean, DBL_MAX, x) *
            I(Y->mean, DBL_MAX, y)
    );
    return res;
}

void skewed_max::cal(double freq) {

    double l_bound = min(X->mean - 3 * X->stddev, Y->mean - 3 * Y->stddev);
    double r_bound = max(X->mean + 3 * X->stddev, Y->mean + 3 * Y->stddev);

    double x = l_bound;
    double dx = (r_bound - l_bound) / freq;
    double dy = (r_bound - l_bound) / freq;
    double one = 0.0;
    double square = 0.0;
    double cube = 0.0;

    for (int i = 0; i < freq; i++) {
        double y = l_bound;
        double one_y = 0.0;
        double square_y = 0.0;
        double cube_y = 0.0;

        for (int j = 0; j < freq; j++) {
            double join = joint_pdf(x, j);
            double m = max(x, y);
            one_y += m * join * dy;
            square_y += pow(m, 2) * join * dy;
            cube_y += pow(m, 3) * join * dy;
            y += dy;
        }
        one += one_y * dx;
        square += square_y * dx;
        cube += cube_y * dx;
        x += dx;
    }

    mean = one;
    variance = square - mean * mean;
    skewness = (cube - 3 * mean * variance - pow(mean, 3)) / pow(variance, 1.5);

}