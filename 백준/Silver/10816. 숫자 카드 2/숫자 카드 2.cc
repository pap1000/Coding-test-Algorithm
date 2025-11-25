#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int upper_index(const vector<int>& a, int b) {	//탐색값의 가장 위쪽 경계를 검색
	int left = 0;
	int right = a.size();
	while (left < right) {
		int mid = (left + right) / 2;
		if (a[mid] <= b) left = mid + 1;	//탐색값보다 같거나 작으면 left를 mid+1로 수정
		else right = mid;	//탐색값보다 크다면 right값을 mid로 수정
	}	//결국 left를 가장 인덱스가 큰 탐색값으로 수정하는 것이 목표, lower는 반대로 가장 작은 인덱스를 찾는 것이 목표
	return left;
}

int lower_index(const vector<int>& a, int b) {
	int left = 0;
	int right = a.size();
	while (left < right) {
		int mid = (left + right) / 2;
		if (a[mid] < b) left = mid + 1;
		else right = mid;
	}
	return left;
}

int binary_search(const vector <int>& a, int b) {	//중복값이 존재하는 배열에서 이진탐색 후 개수를 반환
	auto upper = upper_index(a, b);
	auto lower = lower_index(a, b);
	return upper - lower;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);

	int N, M;
	vector <int> card;
	cin >> N;
	for (int i = 0;i < N;i++) {
		int n;
		cin >> n;
		card.push_back(n);
	}

	sort(card.begin(), card.end());

	cin >> M;
	for (int i = 0;i < M;i++) {
		int m;
		int count = 0;
		cin >> m;
		count = binary_search(card, m);
		cout << count << " ";
	}

	return 0;
}