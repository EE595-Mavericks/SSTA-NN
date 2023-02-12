#include "normal_max.h"
#include "skewed_max.h"

using namespace std;

int main() {
    skewed_rv x(8, 100, 1);
    skewed_rv y(12, 10, 1);
    skewed_max z(&x, &y);
    z.cal(10000);
    cout << z.mean << endl;
    cout << z.variance << endl;
    cout << z.skewness << endl;
}