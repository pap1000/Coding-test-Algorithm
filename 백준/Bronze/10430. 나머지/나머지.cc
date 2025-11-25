#include <iostream>

using namespace std;
int main() {
    int a, b, c;
    int res1, res2, res3, res4;

    cin >> a;
    cin >> b;
    cin >> c;

    res1 = (a + b) % c;
    res2 = ((a % c) + (b % c)) % c;
    res3 = (a * b) % c;
    res4 = ((a % c) * (b % c)) % c;

    cout << res1 << endl;
    cout << res2 << endl;
    cout << res3 << endl;
    cout << res4 << endl;

    return 0;
}