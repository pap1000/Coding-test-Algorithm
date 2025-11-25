#include <iostream>

using namespace std;
int main() {
	int N;
	int M;
	
	cin >> N;
	cin >> M;

	//행렬A
	int **A = new int*[N];
	for (int i = 0;i < N;i++) {
		A[i] = new int[M];
	}
	//행렬B
	int** B = new int* [N];
	for (int i = 0;i < N;i++) {
		B[i] = new int[M];
	}

	for (int i = 0;i < N;i++) {
		for (int j = 0;j < M;j++) {
			cin >> A[i][j];
		}
	}
	for (int i = 0;i < N;i++) {
		for (int j = 0;j < M;j++) {
			cin >> B[i][j];
		}
	}

	for (int i = 0;i < N;i++) {
		for (int j = 0;j < M;j++) {
			cout << A[i][j] + B[i][j] << ' ';
		}
		cout << '\n';
	}

	for (int i = 0; i < N;i++) {
		delete[] A[i];
	}
	delete[] A;

	return 0;
}