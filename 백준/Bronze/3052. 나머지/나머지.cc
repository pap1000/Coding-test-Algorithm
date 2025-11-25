#include <iostream>

using namespace std;
int main() {
	int number[10] = { 0 };
	int remainder[42] = { 0 };
	int count = 0;

	for (int i = 0;i < 10;i++) {
		cin >> number[i];
		int index = number[i] % 42;
		if (remainder[index] != 1) {
			remainder[index] = 1;
			count++;
		}
	}
	cout << count;

	return 0;
}