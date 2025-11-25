#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);

	string str;

	while (true) {
		getline(cin, str);
		if (str == ".") break;

		vector <char> check;	//괄호 앞부분을 저장할 벡터
		bool check_balance = false;

		for (int i = 0;i < str.size();i++) {
			if (str[i] == '(' || str[i] == '[') {
				check.push_back(str[i]);
			}
			else if (str[i] == ')') {
				if (check.empty() || check.back() != '(') {
					check_balance = true;
					break;
				}
				check.pop_back();	//벡터에서 괄호를 제거하여 스택 관리
			}
			else if (str[i] == ']') {
				if (check.empty() || check.back() != '[') {
					check_balance = true;
					break;
				}
				check.pop_back();
			}
		}
		if (check.empty() && !check_balance) cout << "yes" << "\n";	//벡터가 비어있고 균형이 맞았다면
		else cout << "no" << "\n";
	}
	

	return 0;
}