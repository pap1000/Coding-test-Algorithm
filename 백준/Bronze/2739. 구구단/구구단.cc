#include <iostream>

using namespace std;
int main() {
	int a, i;
	i = 1;

	cin >> a;
	while (i < 10) {
		cout << a << " * " << i << " = " << a * i << endl;
		i++;
	}

	return 0;
}