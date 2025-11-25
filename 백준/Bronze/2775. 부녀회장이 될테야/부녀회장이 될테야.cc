#include <iostream>

using namespace std;
int main() {
	int T;
	int k, n;	//층, 호

	cin >> T;
	while (T--) {
		cin >> k >> n;
		int* arr = new int[n];
		for (int i = 0;i < n;i++) arr[i] = i + 1;	//0층
		while (k--) {	//k가 0층이면 무시, 1층 이상이면 추가 연산
			for (int i = n - 1;i >= 0;i--) {
				for (int k = 0; k <= i - 1;k++) {
					arr[i] += arr[k];
				}
			}
		}
		cout << arr[n-1] << "\n";
	}

	return 0;
}