#include <iostream>
#include <string>

using namespace std;
int main() {
	string M;
	int N = 0;
	int MIN = 0;
	int sum = 0;

	cin >> M;
	int lower_int = stoi(M) - 9 * M.size();

	for (int i = lower_int; i < stoi(M); i++) {
		sum = i;
		string lower_M = to_string(i);
		for (int k = 0;k < lower_M.size();k++) {
			sum += lower_M[k]-'0';	//문자열이기 때문에 '0'을 뺄셈
		}
		if (sum == stoi(M)) {
			cout << i;
			break;
		}
		if (i == stoi(M) - 1) cout << 0;
	}

	return 0;
}