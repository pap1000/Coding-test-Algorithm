#include <iostream>

using namespace std;
int main() {
	float M=0;
	int subject_num;

	cin >> subject_num;
	double* grade = new double[subject_num];
	for (int i = 0;i < subject_num;i++) {
		cin >> grade[i];
		if (grade[i] > M) {
			M = grade[i];
		}
	}

	double total = 0.0;
	double average = 0.0;
	for (int i = 0;i < subject_num;i++) {
		total += (grade[i] / M) * 100;
	}
	average = total / subject_num;

	cout << average;

	return 0;
}