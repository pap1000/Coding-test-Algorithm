#include <iostream>

using namespace std;
int main() {
    double A, B;
    double RESULT;
    cin >> A;
    cin >> B;

    RESULT = A / B;
    cout.precision(10);
    cout << RESULT << endl;

    return 0;
}