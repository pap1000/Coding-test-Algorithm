#include <iostream>

using namespace std;
int main() {
	int N = 0;
	int result = 1;

	cin >> N;
	for (int i = N;i > 0; i--) {
		result = result*i;
	}
	cout << result << endl;

	return 0;
}