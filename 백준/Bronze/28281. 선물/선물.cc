#include <iostream>

using namespace std;
int main() {
	int N, X, A;
	int min = 0;
	cin >> N >> X;
	int* Socks_price = new int[N];
	for (int i = 0;i < N;i++) {
		cin >> A;
		Socks_price[i] = A;
		if (i > 0) {
			int total_price = (Socks_price[i - 1] + Socks_price[i]) * X;
			if (min == 0 || total_price < min) {
				min = total_price;
			}
		}
	}
	cout << min;


	return 0;
}