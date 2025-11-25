#include <iostream>
#include <cmath>
#include <vector>
#include <algorithm>

using namespace std;
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);

	int n;
	cin >> n;
	vector<int> difficulty;

	for (int i = 0;i < n;i++) {
		int diff;
		cin >> diff;
		difficulty.push_back(diff);
	}

	sort(difficulty.begin(), difficulty.end());

	int cut = (int)floor(n * 0.15 + 0.5);
	int start = cut;
	int end = n - cut;

	int total = 0;
	for (int i = start;i < end;i++) {
		total += difficulty[i];
	}
	
	int average = (int)floor((double)total / (end - start) + 0.5);
	if (n == 0) cout << 0;
	else cout << average << "\n";

	return 0;
}