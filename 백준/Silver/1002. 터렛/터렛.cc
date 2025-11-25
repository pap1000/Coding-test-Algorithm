#include <iostream>
#include <cmath>
#include <cstdlib>

using namespace std;
int main() {
	int T; //테스트 케이스 수
	int x1 = 0, x2 = 0, y1 = 0, y2 = 0, r1 = 0, r2 = 0; //조규현과 백승환의 x,y 좌표와 각각의 류재명까지의 거리
	double r3 = 0; //조규현과 백승환 사이의 거리

	cin >> T;
	while (T > 0) {
		cin >> x1 >> y1 >> r1 >> x2 >> y2 >> r2;
		r3 = sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2));

		if (r3 == 0 && r1 == r2)
			cout << "-1" << endl;
		else if (r1 + r2 > r3)
			if (abs(r1 - r2) == r3)
				cout << "1" << endl;
			else if (abs(r1 - r2) > r3)
				cout << "0" << endl;
			else
				cout << "2" << endl;
		else if (r1 + r2 == r3)
			cout << "1" << endl;
		else if (r1 + r2 < r3)
			cout << 0 << endl;
		else
			cout << 0 << endl;
		

		T--;
	}
	
	return 0;
}