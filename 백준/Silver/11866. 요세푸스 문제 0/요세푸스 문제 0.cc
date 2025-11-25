#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
int main() {
	int N, K;
	cin >> N >> K;
	
	vector <int> list(N);
	vector <int> result;
	cout << "<";
	for (int i = 0;i < N;i++) {
		list[i] = i + 1;
	}

	int index = 0;
	while (!list.empty()) {
		index = (index + K - 1) % list.size(); //index에서 k-1만큼 이동해야 k번째. vector의 사이즈로 나누면 그에 해당하는 인덱스
		result.push_back(list[index]);	//해당하는 인덱스를 결과 벡터에 푸쉬
		list.erase(list.begin() + index);	//리스트에서 삭제
	}
	for (int i = 0;i < result.size();i++) {
		cout << result[i];
		if (i != result.size() - 1) cout << ", ";
	}
	cout << ">";

	return 0;
}