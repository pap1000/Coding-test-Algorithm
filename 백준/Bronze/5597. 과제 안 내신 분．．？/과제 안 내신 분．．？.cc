#include <iostream>

using namespace std;
int main() {
	bool student_number[30];
	int n = 0;

	for (int i = 0; i < 30; i++) {
		student_number[i] = false;
	}
	for (int j = 0;j < 28;j++) {
		cin >> n;
		student_number[n-1] = true;
	}
	for (int k = 0;k < 30;k++) {
		if (!student_number[k])
			cout << k+1 << '\n';
	}

	return 0;
}