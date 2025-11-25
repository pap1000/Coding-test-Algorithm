#include <iostream>	

using namespace std;
int main() {
	string number;

	while (1) {
		bool p = true;
		cin >> number;
		if (number == "0") break;
		for (int i = 0;i <= (number.size()-1) / 2;i++) {
			if (number[i] == number[number.size() - 1 - i]) continue;
			p = false;
		}
		if (p) cout << "yes" << "\n";
		else cout << "no" << "\n";
	}

	return 0;
}