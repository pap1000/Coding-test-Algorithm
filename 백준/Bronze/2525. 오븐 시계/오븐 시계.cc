#include <iostream>

using namespace std;
int main() {
	int h, m, t;

	cin >> h;
	cin >> m;
	cin >> t;

	if (m + t >= 60) {
		h = (h + (m + t) / 60)%24;
		m = (m + t) % 60;
		cout << h << " " << m << endl;
	}
	else {
		m = m + t;
		cout << h << " " << m << endl;
	}

	return 0;
}