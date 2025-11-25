#include <iostream>

using namespace std;
int main() {
	int n = 0;
	int max = 0;
	int max_index = 0;

	for (int i = 0;i < 9;i++) {
		cin >> n;
		if (n > max) {
			max = n;
			max_index = i;
		}
	}
	cout << max << "\n";
	cout << max_index + 1;

	return 0;
}