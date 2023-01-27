#include <iostream>
#include <string>
#include <random>

using namespace std;

int main()
{
    const int times=1000000;  // number of experiments

    default_random_engine generator1;
    default_random_engine generator2;
    normal_distribution<double> distribution1(5.0,2.0);
    normal_distribution<double> distribution2(4.0,1.0);
    
    double mean = 0.0;

    for (int i=0; i<times; ++i) {
        double num1 = distribution1(generator1);
        double num2 = distribution2(generator2);
        double num_new = max(num1, num2);
        mean += num_new;
    }

    mean = mean / times;
    cout << mean << endl;
    return 0;
}