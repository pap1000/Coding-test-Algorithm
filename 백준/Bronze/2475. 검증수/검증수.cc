#include <iostream>
#include <cmath>
using namespace std;
int main() {
	int arr[5];
	int total = 0;

	for (int i = 0;i < 5;i++) {
		cin >> arr[i];
		total += pow(arr[i], 2);
	}

	cout << total%10;

	return 0;
}