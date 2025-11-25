#include <iostream>

using namespace std;
int main() {
	int num;
	int size[6];
	int set = 0;
	int T, P;

	cin >> num;
	for (int i = 0;i < 6;i++) cin >> size[i];
	cin >> T >> P;
	for (int i = 0;i < 6;i++) {
		if (size[i] != 0 && size[i] % T != 0) set += (size[i] / T) + 1;
		else if (size[i] != 0 && size[i] % T == 0) set += size[i] / T;
	}
	cout << set << "\n";
	cout << num / P << " " << num % P;

	return 0;
}