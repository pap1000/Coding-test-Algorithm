#include <iostream>

using namespace std;
int main() {
    int a, b;
    int res1, res2, res3, res4;

    cin >> a;
    cin >> b;

    res1 = a * (b % 10);
    res2 = a * (((b % 100) - (b%10)) / 10);
    res3 = a * (b / 100);
    res4 = res1 + (res2 * 10) + (res3 * 100);

    cout << res1 << endl;
    cout << res2 << endl;
    cout << res3 << endl;
    cout << res4 << endl;


    return 0;
}