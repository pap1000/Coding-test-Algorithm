#include <sstream>
#include <iostream>

using namespace std;
int main() {
	int N, v;
	int count = 0;
	string str;

	cin >> N;
	
	cin.ignore();
	getline(cin, str);

	int* a = new int[N];
	stringstream s(str);
	for (int i = 0; i < N; i++) {
		s >> a[i];
	}

	cin >> v;
	for (int i = 0;i < N;i++) {
		if (a[i] == v)
			count++;
	}

	cout << count << endl;

	return 0;
}