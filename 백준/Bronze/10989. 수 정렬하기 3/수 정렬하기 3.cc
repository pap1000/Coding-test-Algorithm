#include <iostream>

using namespace std;
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int N;
	int count[10000] = { 0 };
	cin >> N;

	for (int i = 0;i < N;i++) {
		int n = 0;
		cin >> n;
		count[n-1]++;
	}
	for (int i = 0;i < 10000;i++) {
		for (int k = 0;k < count[i];k++) {
			cout << i + 1 << "\n";
		}
	}

	return 0;
}