N, M = map(int, input().split())
min_total = 64

board = [1 if char == 'W' else 0 for _ in range(N) for char in input()]
# N개가 있다면 0, N-8
for i in range(N-7):
    for k in range(M-7):
        count = 0
        for r in range(i, i+8): # 첫 row 좌표
            for c in range(k, k+8): # 첫 col 좌표
                if (r+c)%2 ==0: # 좌표합이 짝수일 때 W여야 한다고 가정
                    if board[r*M+c]!=1: # W가 아니라면
                        count+=1
                else: # r+c가 홀수일 때 B가 아니라면
                    if board[r*M+c]!=0:
                        count+=1
        result = min(count, 64-count)
        min_total = min(min_total, result)
print(min_total)