#include <iostream>

using namespace std;
int main() {
	int a, b;
	
	//조건문 내에 cin을 넣으면 cin이 데이터를 읽는데 성공하면 true, 실패하면 false를 반환
	while (cin >> a >> b) {
		cout << a + b << "\n";
	}

	return 0;
}