#include <iostream>

using namespace std;
int count_block(char **board, int a, int b) {
	int repaint1 = 0;
	int repaint2 = 0;

	for (int i = 0;i < 8;i++) {
		for (int j = 0;j < 8;j++) {
			char expected = ((i + j) % 2 == 0) ? 'B' : 'W';	//i와 j의 합은 떨어진 칸 수 = 색이 변해야 하는 횟수 -> 2번 변하면 원래 색으로 복귀
			if (expected != board[a + i][b + j]) repaint1++;
			expected = ((i + j) % 2 == 0) ? 'W' : 'B';	//시작점이 W인 경우
			if (expected != board[a + i][b + j]) repaint2++;
		}
	}
	return min(repaint1, repaint2);
}

int main() {
	int N, M;
	cin >> N >> M;
	char** board = new char *[N];	//NXM 2차원 배열

	for (int i = 0;i < N;i++) {
		board[i] = new char[M];
	}

	for (int i = 0;i < N;i++) {
		for (int j = 0;j < M;j++) {
			cin >> board[i][j];
		}
	}

	int MIN = 64;	//모든 칸을 다시 칠하는 최악의 경우
	for (int i = 0;i < N-8+1;i++) {
		for (int j = 0;j < M-8+1;j++) {
			int repaint = count_block(board, i, j);
			if (i == 0 && j == 0) {
				MIN = repaint;
				continue;
			}
			if (repaint < MIN) MIN = repaint;
		}
	}
	cout << MIN;

	return 0;
}