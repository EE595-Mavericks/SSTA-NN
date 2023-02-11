#include <iostream>
#include <cmath>
#include <chrono>
#include <random>
#include <boost/random/mersenne_twister.hpp>
#include <boost/random/uniform_real_distribution.hpp>
#include <boost/math/special_functions/erf.hpp>

// CDF of the skew normal distribution
double CDF_skewnormal(double x, double alpha) {
  return 2.0 * (1.0 + boost::math::erf(alpha * x / std::sqrt(2.0))) / 2.0 - 1.0;
}

// Inverse CDF of the skew normal distribution
double CDF_skewnormal_inv(double u, double alpha) {
  return std::sqrt(2.0) * boost::math::erf_inv(2.0 * u - 1.0) / alpha;
}

// Compute shape parameter from mean, variance, and skewness
double compute_alpha(double mean, double variance, double skewness) {
  return skewness * std::sqrt(variance) / std::pow(1.0 + skewness * skewness, 1.5);
}

int main() {
  boost::random::mt19937 gen1(std::random_device{}());

  boost::random::mt19937 gen2(std::random_device{}());

  boost::random::uniform_real_distribution<double> uniform(0.0, 1.0);

  double mean1 = 8.0;
  double variance1 = 100.0;
  double skewness1 = 1;

  double mean2 = 12.0;
  double variance2 = 10.0;
  double skewness2 = 1.0;

  double alpha1 = compute_alpha(mean1, variance1, skewness1);
  double alpha2 = compute_alpha(mean2, variance2, skewness2);

  double total = 0.0;

  for (int i = 0; i < 1000000; ++i) {
    double u1 = uniform(gen1);
    double u2 = uniform(gen2);

    double x1 = mean1 + std::sqrt(variance1) * CDF_skewnormal_inv(u1, alpha1);
    double x2 = mean2 + std::sqrt(variance2) * CDF_skewnormal_inv(u2, alpha2);

    double x = std::max(x1, x2);
    
    total += x;
  }

  double mean  = total / 1000000;

  std::cout << "mean = " << mean << std::endl;
  return 0;
}
