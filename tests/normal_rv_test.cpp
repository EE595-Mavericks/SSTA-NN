#include <iostream>
#include <string>
#include <random>

using namespace std;

int main(int argc, char *argv[]) {

    const int times=1000000;  // number of experiments

    double muX = atof(argv[1]);
    double varX = atof(argv[2]);
    double muY = atof(argv[3]);
    double varY = atof(argv[4]);

    double stddevX = pow(varX, 0.5);
    double stddevY = pow(varY, 0.5);

    default_random_engine generator1;
    default_random_engine generator2;
    normal_distribution<double> distribution1(muX,stddevX);
    normal_distribution<double> distribution2(muY,stddevY);
    
    double mean_z = 0.0;
    double square_z = 0.0;
    double cube_z = 0.0;
    double variance_z = 0.0;
    double skewness_z = 0.0;

    for (int i=0; i<times; ++i) {
        double num1 = distribution1(generator1);
        double num2 = distribution2(generator2);
        double z = max(num1, num2);
        mean_z += z;
        square_z += pow(z, 2);
        cube_z += pow(z, 3);
    }

    mean_z = mean_z / times;
    square_z = square_z / times;
    cube_z = cube_z / times;

    variance_z = square_z - pow(mean_z, 2);
    skewness_z = (cube_z - 3*mean_z*variance_z - pow(mean_z, 2)) / pow(variance_z, 1.5);

    cout << mean_z << endl;
    cout << variance_z << endl;
    cout << skewness_z << endl;
    return 0;
}