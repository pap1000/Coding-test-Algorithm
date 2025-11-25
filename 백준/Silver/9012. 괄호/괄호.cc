#include <iostream>
#include <vector>

using namespace std;
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);

	int T;
	cin >> T;
	while (T--) {
		string str;
		bool VPS = true;
		cin >> str;
		int count = 0;
		for (int i = 0;i < str.size();i++) {
			if (str[i] == '(') count++;
			else if (str[i] == ')') count--;
			if (count < 0) VPS = false;
		}
		if (count==0&&VPS) cout << "YES" << "\n";
		else cout << "NO" << "\n";
	}

	return 0;
}