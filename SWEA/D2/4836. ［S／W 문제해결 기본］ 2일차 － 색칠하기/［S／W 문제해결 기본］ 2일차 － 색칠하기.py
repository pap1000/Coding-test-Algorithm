T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    board = [[0] * 10 for _ in range(10)]
    check_board = [[0] * 10 for _ in range(10)]

    for i in range(n):
        x1, y1, x2, y2, col = list(map(int, input().split()))
        for j in range(x1, x2 +1):
            for k in range(y1, y2 + 1):
                curr = board[j][k]
                if curr != 0 and curr != col:
                    check_board[j][k] = 1
                else:
                    board[j][k] = col
                    
    answer = 0
    for i in range(10):
        answer += sum(check_board[i])
                    
    print(f"#{test_case} {answer}")