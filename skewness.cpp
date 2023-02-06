#include <cmath>
#include <iostream>
#include "float.h"
#include "unordered_set"

using namespace std;


double muX, sigmaX, varX, gammaX;
double muY, sigmaY, varY, gammaY;

double phi(double x, double y) {
    double res = exp(-(pow(x, 2) + pow(y, 2)) / 2);
    return res;
}

int I(double down, double up, double target) {
    return target < up && target > down ? 1 : 0;
}

void integral(double start, double end, double freq, double &mean, double &variance, double &skewness) {
    double dx = (end - start) / freq;
    double dy = (end - start) / freq;
    double x = start;
    double y = start;
    double one = 0.0;
    double square = 0.0;
    double cube = 0.0;
    double tau = M_PI / 2 * (gammaX + 1 / gammaX) * (gammaY + 1 / gammaY);
    double sigma_x_l = sigmaX / gammaX;
    double sigma_y_l = sigmaY / gammaY;
    double sigma_x_r = sigmaX * gammaX;
    double sigma_y_r = sigmaY * gammaY;
    double f_gamma, m;

    for (int i = 0; i < freq; i++) {
        double one_y = 0.0;
        double square_y = 0.0;
        double cube_y = 0.0;
        y = start;

        for (int j = 0; j < freq; j++) {
            f_gamma = 1 / (tau * sigmaX * sigmaY) * (
                    phi((x - muX) / sigma_x_l, (y - muY) / sigma_y_l) *
                    I(-DBL_MAX, muX, x) *
                    I(-DBL_MAX, muY, y) +
                    phi((x - muX) / sigma_x_l, (y - muY) / sigma_y_r) *
                    I(-DBL_MAX, muX, x) *
                    I(muY, DBL_MAX, y) +
                    phi((x - muX) / sigma_x_r, (y - muY) / sigma_y_l) *
                    I(muX, DBL_MAX, x) *
                    I(-DBL_MAX, muY, y) +
                    phi((x - muX) / sigma_x_r, (y - muY) / sigma_y_r) *
                    I(muX, DBL_MAX, x) *
                    I(muY, DBL_MAX, y)
            );

            m = max(x, y);
            one_y += m * f_gamma * dy;
            square_y += pow(m, 2) * f_gamma * dy;
            cube_y += pow(m, 3) * f_gamma * dy;
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


int main(int argc, char *argv[]) {

    muX = atof(argv[1]);
    varX = atof(argv[2]);
    gammaX = atof(argv[3]);
    muY = atof(argv[4]);
    varY = atof(argv[5]);
    gammaY = atof(argv[6]);
    sigmaX = sqrt(varX);
    sigmaY = sqrt(varY);

    double mean = 0.0;
    double variance = 0.0;
    double skewness = 0.0;

    double left_integral_bound = min(muX - 10 * pow(varX, 0.5), muY - 10 * pow(varY, 0.5));
    double right_integral_bound = max(muX + 10 * pow(varX, 0.5), muY + 10 * pow(varY, 0.5));

    cout << "left_integral_bound: " << left_integral_bound << endl;
    cout << "right_integral_bound: " << right_integral_bound << endl;

    integral(left_integral_bound, right_integral_bound, 10000, mean, variance, skewness);

    cout << "mean = " << mean << endl;
    cout << "variance = " << variance << endl;
    cout << "skewness = " << skewness << endl;

    return 0;
}
