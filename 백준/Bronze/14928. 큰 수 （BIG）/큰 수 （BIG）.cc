#include <iostream>
#include <string>

using namespace std;

int divideNumber(string number, int divisor) {
	string quotient = "";
	int remainder = 0;

	for (char digit : number) {	//문자로 된 숫자를 한자리씩 읽어옴
		int current = remainder * 10 + (digit - '0'); //읽어온 문자를 수로 변환 후 이전에 남아있던 값을 한자릿수 올림
		quotient += (current / divisor) + '0';	//문자열에 몫을 저장. 한글자씩 추가되므로 자릿수 올림은 필요없음.
		remainder = current % divisor;	//나머지
	}
	size_t pos = quotient.find_first_not_of('0');	//0이 아닌 첫번째 수의 위치
	
	if (pos != string::npos)
		quotient = quotient.substr(pos);
	else //모두 0으로 된 경우
		quotient = "0";

	return remainder;
}

int main() {
	string N;
	int n = 20000303;
	int remainder = 0;

	cin >> N;

	remainder = divideNumber(N, n);

	cout << remainder;

	return 0;
}