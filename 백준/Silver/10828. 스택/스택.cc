#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);


	vector <string> stack;
	int N;
	cin >> N;
	cin.ignore();

	while (N--) {
		string command;
		getline(cin, command);
		if (command.substr(0, 4) == "push") {
			string to_push = command.substr(5, command.size() - 1);
			stack.push_back(to_push);
		}
		else if (command == "pop") {
			if (stack.empty()) cout << -1 << "\n";
			else {
				cout << stack.back() << "\n";
				stack.pop_back();
			}
		}
		else if (command == "size") cout << stack.size() << "\n";
		else if (command == "empty") {
			if (stack.empty()) cout << 1 << "\n";
			else cout << 0 << "\n";
		}
		else if (command == "top") {
			if (stack.empty()) cout << -1 << "\n";
			else cout << stack.back() << "\n";
		}
	}

	return 0;
}