#include <iostream>
#include <vector>
#include <string>
#include <cctype>
#include <unordered_map>
#include <algorithm>

using namespace std;
bool isNumber(string s) {
	return !s.empty() && all_of(s.begin(), s.end(), ::isdigit);
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);

	int N, M;
	string name;
	vector <string> list;
	unordered_map<string, int> nameToIndex;	//키와 값을 쌍으로 저장. 여기서는 이름과 순서(번호)

	cin >> N >> M;

	for (int i = 0;i < N;i++) {
		cin >> name;
		list.push_back(name);
		nameToIndex[list[i]] = i+1;
	}

	while (M--) {
		string quiz;
		cin >> quiz;
		if (isNumber(quiz)) {
			int idx = stoi(quiz);
			cout << list[idx-1] << "\n";
		}
		else {
			cout << nameToIndex[quiz] << "\n";
		}
	}

	return 0;
}