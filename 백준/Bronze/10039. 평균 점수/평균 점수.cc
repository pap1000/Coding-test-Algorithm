#include <iostream>

using namespace std;
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);

	int N = 5;
	int total = 0;
	while (N--) {
		int score = 0;
		cin >> score;
		if (score < 40) {
			score = 40;
			total += score;
			continue;
		}
		else total += score;
	}
	cout << total / 5;

	return 0;
}