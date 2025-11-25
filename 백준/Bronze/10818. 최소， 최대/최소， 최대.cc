#include <iostream>

using namespace std;
int main() {
	int N, n;
	int max, min;
	
	cin >> N;
	cin >> n;
	max = n;
	min = n;
	for (int i = 0;i < N-1;i++) {
		cin >> n;
		if (n > max) max = n;
		if (n < min) min = n;
	}
	cout << min << " " << max;
	return 0;
}