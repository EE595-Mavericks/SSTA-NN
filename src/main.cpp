#include "normal_max.h"
#include "skewed_max.h"

using namespace std;

int main() {
    skewed_rv x(1, 1, 1);
    skewed_rv y(1, 1, 1);
    skewed_max z(&x, &y);
}