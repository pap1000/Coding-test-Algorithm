#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

int mean(vector <int>& a) {
	int total = 0;
	for (int i = 0;i < a.size();i++) {
		total += a[i];
	}
	int average = floor(((double)total / a.size()) + 0.5);
	return average;
}

int mode(vector <int>& a) {
	int count = 0;
	int mode = 0;
	bool more_exist = false;;
	for (int i = 0;i < a.size();i++) {
		if (i!=0&&a[i - 1] == a[i]) continue;
		auto lower = lower_bound(a.begin(), a.end(), a[i]);
		auto upper = upper_bound(a.begin(), a.end(), a[i]);
		if (count < upper - lower+1) {	//더 많이 발견된 경우
			count = upper - lower+1;
			mode = a[i];
			more_exist = false;
		}
		else if (count == upper - lower + 1&&!more_exist) {	//최대 빈도수와 같고 이전에 이런 수가 없던 경우
			mode = a[i];
			more_exist = true;
		}
	}
	return mode;
}



int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);

	vector <int> list;
	int N;
	cin >> N;


	for (int i = 0;i < N;i++) {
		int M;
		cin >> M;
		list.push_back(M);
	}
	sort(list.begin(), list.end());
	cout << mean(list) << "\n";
	cout << list[(list.size() / 2)] << "\n";
	cout << mode(list) << "\n";
	cout << list[list.size() - 1] - list[0] << "\n";

	return 0;
}