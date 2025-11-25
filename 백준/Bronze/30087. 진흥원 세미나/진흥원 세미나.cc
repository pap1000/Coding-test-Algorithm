#include <iostream>

using namespace std;
int main() {
	string seminar[7] = {"Algorithm", "DataAnalysis", "ArtificialIntelligence", "CyberSecurity", "Network", "Startup", "TestStrategy"};
	string room[7] = {"204", "207", "302", "B101", "303", "501", "105"};
	int N;
	
	cin >> N;
	string* list = new string[N];
	for (int i = 0;i < N;i++) {
		cin >> list[i];
	}


	for (int j = 0;j < N;j++) {
		for (int i = 0;i < 7;i++) {
			if (list[j] == seminar[i]) {
				cout << room[i] << "\n";
			}
		}
	}

	return 0;
}