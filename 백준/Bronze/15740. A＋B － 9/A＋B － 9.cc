#include <iostream>
#include <vector>
#include <algorithm> // reverse 사용을 위해 필요

using namespace std;

// 문자열을 숫자 벡터로 바꾸는 함수
vector<int> getnumber(string A, int M) {
	vector<int> va;
	for (int i = 0; i < M; i++) {
		va.push_back(i < A.size() ? A[A.size() - i - 1] - '0' : 0);
	}
	return va;
}

// 두 벡터 숫자를 비교해서 A >= B 여부를 판단하는 함수
bool is_AB_greater_equal(const vector<int>& A, const vector<int>& B) {
	for (int i = A.size() - 1; i >= 0; i--) {
		if (A[i] > B[i]) return true;
		else if (A[i] < B[i]) return false;
	}
	return true; // 같을 경우 포함
}

// 전체 연산 결과의 부호를 정하는 함수
bool decision_sign(const vector<int>& A, const vector<int>& B, bool A_sign, bool B_sign) {
	if (A_sign && B_sign) return true;
	if (!A_sign && !B_sign) return false;
	if (A_sign && !B_sign) return true;
	if (!A_sign && B_sign) {
		return is_AB_greater_equal(B, A); // B가 크면 양수
	}
	return true; // 기본값
}

// 덧셈 함수
vector<int> sumnumber(const vector<int>& A, const vector<int>& B) {
	vector<int> result;
	int carry = 0;

	for (int i = 0; i < A.size(); i++) {
		int sum = A[i] + B[i] + carry;
		result.push_back(sum % 10);
		carry = sum / 10;
	}
	if (carry) result.push_back(carry);
	return result;
}

// 뺄셈 함수, A >= B 라고 가정
vector<int> subnumber(const vector<int>& A, const vector<int>& B) {
	vector<int> result;
	int borrow = 0;

	for (int i = 0; i < A.size(); i++) {
		int diff = A[i] - B[i] - borrow;
		if (diff < 0) {
			result.push_back(diff + 10);
			borrow = 1;
		}
		else {
			result.push_back(diff);
			borrow = 0;
		}
	}
	return result;
}

int main() {
	vector<int> va, vb, result;
	string A, B;
	bool A_sign = true;
	bool B_sign = true;

	cin >> A >> B;

	// 부호 처리
	if (A[0] == '-') {
		A = A.substr(1);
		A_sign = false;
	}
	if (B[0] == '-') {
		B = B.substr(1);
		B_sign = false;
	}

	// 벡터화 (자릿수 맞추기)
	int M = max(A.size(), B.size());
	va = getnumber(A, M);
	vb = getnumber(B, M);

	// 연산 결과의 부호 판단
	bool result_sign = true;
	if (A_sign == B_sign) {
		result_sign = A_sign;
		result = sumnumber(va, vb);
	}
	else {
		if (is_AB_greater_equal(va, vb)) {
			result = subnumber(va, vb);
			result_sign = A_sign;
		}
		else {
			result = subnumber(vb, va);
			result_sign = B_sign;
		}
	}

	// 자릿수 뒤집기
	reverse(result.begin(), result.end());

	// 0만 있는 경우 처리
	bool is_zero = all_of(result.begin(), result.end(), [](int d) { return d == 0; });

	if (is_zero) {
		cout << "0\n";
		return 0;
	}

	// 부호 출력
	if (!result_sign) cout << "-";

	// 앞자리 0 제거하며 출력
	bool first = true;
	for (int d : result) {
		if (first && d == 0) continue;
		first = false;
		cout << d;
	}
	cout << endl;

	return 0;
}
