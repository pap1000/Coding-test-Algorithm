T = int(input())
for test_case in range(1, T + 1):
    answer = ""
    n, m = map(int, input().split())
    board = [input() for _ in range(n)]
    
    for i in range(n):
        for j in range(n - m + 1):
            row = board[i][j:j+m]
            col = "".join(board[k][i] for k in range(j, j + m))
            
            if row == row[::-1]:
                answer = row
                break
                
            if col == col[::-1]:
                answer = col
                break
                
    print(f"#{test_case} {answer}")