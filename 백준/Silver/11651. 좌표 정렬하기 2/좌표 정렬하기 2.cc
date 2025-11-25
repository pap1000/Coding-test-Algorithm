#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);

	int N;
	cin >> N;
	vector<pair<int, int>> point(N);
	for (int i = 0;i < N;i++) {
		cin >> point[i].second >> point[i].first;
	}
	sort(point.begin(), point.end());
	
	for (int i = 0;i < N;i++) {
		cout << point[i].second << " " << point[i].first << "\n";
	}

	return 0;
}