#include <iostream>
#include <vector>

using namespace std;
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);

	int k;
	cin >> k;
	vector <int> list;
	for (int i = 0;i < k;i++) {
		int n = 0;
		cin >> n;
		if (n == 0) {
			list.pop_back();
			continue;
		}
		list.push_back(n);
	}

	int result = 0;
	int time = list.size();
	while(time--){
		result += list.back();
		list.pop_back();
	}
	cout << result;

	return 0;
}