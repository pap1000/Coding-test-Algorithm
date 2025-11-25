#include <iostream>

using namespace std;
int main() {
    int A, B;
    int add, sub, times, quotient, remainder;
    cin >> A;
    cin >> B;

    add = A + B;
    sub = A - B;
    times = A * B;
    quotient = A / B;
    remainder = A % B;

    cout << add << endl;
    cout << sub << endl;
    cout << times << endl;
    cout << quotient << endl;
    cout << remainder << endl;

    return 0;
}