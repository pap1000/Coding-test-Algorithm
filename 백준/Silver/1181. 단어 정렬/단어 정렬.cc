#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

bool cmp(const string& a, const string& b) {
	if (a.length() == b.length()) return a < b;
	return a.length() < b.length();
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	int N;
	cin >> N;
	vector<string> word(N);

	for (int i = 0;i < N;i++) {
		cin >> word[i];
	}

	sort(word.begin(), word.end(), cmp);
	word.erase(unique(word.begin(), word.end()), word.end());	//unique는 중복이 시작되는 지점을 리턴. erase로 중복되는 값들을 제거
	for (const string& s : word) {
		cout << s << "\n";
	}
	return 0;
}