#include <iostream>

using namespace std;
int main() {
	int h, m;

	cin >> h;
	cin >> m;

	if (h != 0) {
		if (m >= 45)
			cout << h << " " << m - 45;
		else
			cout << h - 1 << " " << 15 + m;
	}
	else
		if (m >= 45)
			cout << h << " " << m - 45;
		else
			cout << 23 << " " << 15 + m;

	return 0;
}