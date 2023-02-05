#include <cmath>
#include <iostream>
#include "float.h"

using namespace std;


double mu1;
double sigma1;
double var1;
double mu2;
double sigma2;
double var2;

double phi(double t) {
    double exponent = -pow(t, 2) / 2;
    return (1.0 / (sqrt(2.0 * M_PI))) * exp(exponent);
}

double big_phi(double w) {
    return 0.5 * (1.0 + erf(w / sqrt(2.0)));
}

double f1(double x) {
    double res;
    res = 1 / sigma1 * phi((x + mu1) / sigma1) * big_phi((x + mu2) / sigma2);
    return res;
}

double f2(double x) {
    double res;
    res = 1 / sigma2 * phi((x + mu2) / sigma2) * big_phi((x + mu1) / sigma1);
    return res;
}

double pdf_z(double z) {
    return f1(-z) + f2(-z);
}

double integral(double start, double end, double freq) {
    double step = (end - start) / freq;
    cout << step << endl;
    double res = 0;
    double x = start;
    for (int i = 0; i < freq; i++) {
        res += x * pdf_z(x);
        x += step;
    }
    return res;
}

int main(int argc, char *argv[]) {

    mu1 = atof(argv[1]);
    var1 = atof(argv[2]);
    mu2 = atof(argv[3]);
    var2 = atof(argv[4]);
    sigma1 = sqrt(var1);
    sigma2 = sqrt(var2);

//    cout << integral(-100, 100, 100000) << endl;
    cout << pdf_z(-10) << endl;

    return 0;
}
