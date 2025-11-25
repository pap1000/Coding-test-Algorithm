#include <iostream>

using namespace std;
int main() {
	int count = 0;
	int present = 0;
	int previous = 0;

	cin >> present;
	for (int i = 0;i < 7;i++) {
		previous = present;
		cin >> present;
		if (present - previous == 1) count++;
		else if(present - previous == -1) count--;
	}
	if (count == 7) cout << "ascending";
	else if (count == -7) cout << "descending";
	else cout << "mixed";

	return 0;
}