#include <iostream>
#include <string>

using namespace std;
int main() {
	string S;
	int T, R;

	cin >> T;
	while (T--) {
		cin >> R;
		cin.ignore();
		getline(cin, S);
		for (int i = 0;i < S.size();i++) {
			for (int k = 0;k < R;k++) cout << S[i];
		}
		cout << "\n";
	}

	return 0;
}