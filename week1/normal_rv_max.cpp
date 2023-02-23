#include <cmath>
#include <iostream>

using namespace std;

double pdf(double t) {
    double exponent = -pow(t, 2) / 2;
    return (1.0 / (sqrt(2.0 * M_PI))) * exp(exponent);
}

double cdf(double w) {
    return 0.5 * (1.0 + erf(w / sqrt(2.0)));
}

int main(int argc, char *argv[]) {

    double muX = atof(argv[1]);
    double varX = atof(argv[2]);
    double muY = atof(argv[3]);
    double varY = atof(argv[4]);

    double mu_sum = muX + muY;
    double var_sum = varX + varY;

    double a = sqrt(varX + varY);
    double alpha = (muX - muY) / a;
    double E_Z = muX * cdf(alpha) + muY * cdf(-alpha) + a * pdf(alpha);
    double E_Z2 = (varX + pow(muX, 2)) * cdf(alpha) +
                  (varY + pow(muY, 2)) * cdf(-alpha) +
                  (muX + muY) * a * pdf(alpha);
    double var_z = E_Z2 - pow(E_Z, 2);

    // cout << "mu_sum = " << mu_sum << endl;
    // cout << "var_sum = " << var_sum << endl;
    // cout << "mu_max = " << E_Z << endl;
    // cout << "var_max = " << var_z << endl;

    printf("%.10f %.10f\n", E_Z, var_z);


    return 0;
}
