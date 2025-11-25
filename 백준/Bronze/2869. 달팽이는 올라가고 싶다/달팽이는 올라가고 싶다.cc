#include <iostream>

using namespace std;
int main() {
	int A, B, V;
	int day = 0;

	cin >> A >> B >> V;
	V -= A;
	day = V/(A - B);
	if (V % (A - B) != 0) day++;
	cout << ++day;

	return 0;
}