#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);

	int M, N;
	cin >> M >> N;
	
	vector<bool> is_prime(N + 1, true);
	is_prime[0] = false;
	is_prime[1] = false;

	for (int i = 2; i <= sqrt(N);i++) {
		if (is_prime[i]) {
			for (int j = i * i;j <= N;j += i) {
				is_prime[j] = false;
			}
		}
	}

	for (int i = M;i <= N;i++) {
		if (is_prime[i]) {
			cout << i << "\n";
		}
	}

	return 0;
}