#include <iostream>

using namespace std;
int main() {
	int a, b, sum;
	sum = 0;
	do{
		cin >> a;
		cin >> b;
		sum = a + b;
		if(sum!=0)
			cout << sum << endl;
	} while (sum != 0);

	return 0;
}