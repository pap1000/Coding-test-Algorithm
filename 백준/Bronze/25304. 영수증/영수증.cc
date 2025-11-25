#include <iostream>

using namespace std;
int main() {
	int total, N, price, count, sum;

	sum = 0;
	cin >> total;
	cin >> N;
	while (N > 0) {
		cin >> price;
		cin >> count;
		sum += price * count;
		N--;
	}

	if (total == sum)
		cout << "Yes" << endl;
	else
		cout << "No" << endl;

	return 0;
}