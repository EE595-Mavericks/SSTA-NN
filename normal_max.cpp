

class max_normal {
public:
    max_normal(normal_rv) {
        sigma1 = sqrt(var1);
        sigma2 = sqrt(var2);
    }

    ~max_normal();

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
        res = 1 / sigma1 * phi((x + mu1) / sigma1) * big_phi(-(x + mu2) / sigma2);
        return res;
    }

    double f2(double x) {
        double res;
        res = 1 / sigma2 * phi((x + mu2) / sigma2) * big_phi(-(x + mu1) / sigma1);
        return res;
    }

    double pdf_z(double z) {
        return f1(-z) + f2(-z);
    }

    void integral(double start, double end, double freq, double &mean, double &variance, double &skewness) {
        double step = (end - start) / freq;
        double x = start;
        double x_square_mean = 0.0;
        double x_cube_mean = 0.0;

        for (int i = 0; i < freq; i++) {
            mean += x * pdf_z(x) * step;
            x_square_mean += x * x * pdf_z(x) * step;
            x_cube_mean += x * x * x * pdf_z(x) * step;
            x += step;
        }

        variance = x_square_mean - mean * mean;
        skewness = (x_cube_mean - 3 * mean * variance - pow(mean, 3)) / pow(variance, 1.5);

        return;
    }

};


int main(int argc, char *argv[]) {

    mu1 = atof(argv[1]);
    var1 = atof(argv[2]);
    mu2 = atof(argv[3]);
    var2 = atof(argv[4]);
    sigma1 = sqrt(var1);
    sigma2 = sqrt(var2);

    double mean = 0.0;
    double variance = 0.0;
    double skewness = 0.0;

    double left_integral_bound = min(mu1 - 10 * pow(var1, 0.5), mu2 - 10 * pow(var2, 0.5));
    double right_integral_bound = max(mu1 + 10 * pow(var1, 0.5), mu2 + 10 * pow(var2, 0.5));
    integral(left_integral_bound, right_integral_bound, 100000, mean, variance, skewness);

    cout << "mean = " << mean << endl;
    cout << "variance = " << variance << endl;
    cout << "skewness = " << skewness << endl;

    return 0;
}