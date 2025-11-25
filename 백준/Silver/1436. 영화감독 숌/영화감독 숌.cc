#include <iostream>
#include <string>

using namespace std;
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	int N = 666;
	int M = 0;
	int count = 0;

	cin >> M;
	while (true) {
		if (to_string(N).find("666") != string::npos) {	//브루트포스 알고리즘
			count++;
			if (count == M) {
				cout << N;
				break;
			}
		}
		N++;
	}

	return 0;
}