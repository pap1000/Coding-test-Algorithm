#include <iostream>
#include <vector>

using namespace std;
int main() {
	int N, K = 0;
	cin >> N >> K;

	vector <pair<int, int>> price_tag(N);
	vector <int> max_value(K + 1, 0);

	for(int i=0;i<N;i++) {
		int weight, value;
		cin >> weight >> value;
		price_tag[i] = { weight, value };
	}

	
	for (int i=0;i<N;i++) {
		int weight, value;
		weight = price_tag[i].first;
		value = price_tag[i].second;
		for (int j = K;j > weight - 1;j--) {
			max_value[j] = max(max_value[j], max_value[j - weight] + value);
		}
	}
	cout << max_value[K];

	return 0;
}