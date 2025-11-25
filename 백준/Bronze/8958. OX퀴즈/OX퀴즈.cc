#include <iostream>

using namespace std;
int main() {
	string str;
	int T = 0;

	cin >> T;
	while (T--) {
		int count = 0;
		int score = 0;
		cin >> str;
		for (int i = 0;i < str.size();i++) {
			if (str[i] == 'O') {
				count++;
				score += count;
			}
			else if (str[i] = 'X') count = 0;
		}
		cout << score << "\n";
	}
	return 0;
}