#include <iostream>
#include <string>

using namespace std;
int main() {
	int A, B, C;
	int result;
	int arr[10] = { 0 };
	string str;

	cin >> A >> B >> C;
	result = A * B * C;
	str = to_string(result);

	for (char c : str) {
		int n = c - '0';
		arr[n]++;
	}

	for(int i=0;i<10; i++) cout << arr[i] << "\n";

	return 0;
}