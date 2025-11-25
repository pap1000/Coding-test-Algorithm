#include <iostream>

using namespace std;
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);

	string ISBN;
	cin >> ISBN;
	int check = 0;
	int damaged_index = 0;

	for (int i = 0;i < ISBN.size();i++) {
		if (ISBN[i] != '*') {
			int weight = 0;
			if (i%2==0) weight = 1;
			else weight = 3;
			check += (ISBN[i] - '0')*weight;
		}
		else {
			damaged_index = i;
		}
	}

	int restore = 0;
	if (damaged_index % 2 != 0) {	//짝수번째가 아니면
		restore = (10 - check % 10);
		for (int i = 0;i < 10;i++) {
			if ((i * 3) % 10 == restore) {
				restore = i;
				break;
			}
		}
	}
	else {
		restore = (10 - check % 10);
		
	}
	cout << restore%10;

	return 0;
}