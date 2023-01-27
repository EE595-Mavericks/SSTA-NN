#include <cmath>
#include <iostream>

double cdf(double x, double mean = 0, double stddev = 1) {
    return 0.5 * (1.0 + std::erf((x - mean) / (stddev * std::sqrt(2.0))));
}

double pdf(double x, double mean = 0, double stddev = 1) {
    double exponent = -1.0 * std::pow(x - mean, 2.0) / (2.0 * std::pow(stddev, 2.0));
    return (1.0 / (stddev * std::sqrt(2.0 * M_PI))) * std::exp(exponent);
}

int main(int argc, char *argv[]) {

    double mu1 = atof(argv[1]);
    double var1 = atof(argv[2]);
    double mu2 = atof(argv[3]);
    double var2 = atof(argv[4]);
    double cita = pow(var1 + var2, 0.5);

    double mu_sum = mu1 + mu2;
    double var_sum = var1 + var2;

    double e_x = mu1 * cdf((mu2 - mu1) / cita, 0, 1) + mu2 * cdf((mu1 - mu2) / cita, 0, 1)
                 + cita * pdf((mu1 - mu2) / cita, 0, 1);
    double e_x2 = (var1 + pow(mu1, 2)) * cdf((mu1 - mu2) / cita, 0, 1) +
                  (var2 + pow(mu2, 2)) * cdf((mu2 - mu1) / cita, 0, 1) +
                  (mu1 + mu2) * cita * pdf((mu1 - mu2) / cita, 0, 1);
    double var_max = e_x2 - pow(e_x, 2);

    std::cout << "mu_sum = " << mu_sum << std::endl;
    std::cout << "var_sum = " << var_sum << std::endl;
    std::cout << "mu_max = " << e_x << std::endl;
    std::cout << "var_max = " << var_max << std::endl;

    return 0;
}