#include "normal_max.h"
#include "skewed_max.h"

using namespace std;

int main() {
    normal_rv x(5, 10);
    normal_rv y(5, 20);
    normal_max z(&x, &y);
    z.cal(10000);
    cout << z.mean << endl;
    cout << z.variance << endl;
    cout << z.skewness << endl;
}