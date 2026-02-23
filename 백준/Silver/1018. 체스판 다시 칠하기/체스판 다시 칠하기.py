N, M = map(int, input().split())
board = [1 if char == 'W' else 0 for _ in range(N) for char in input()] # W=1 B=0

S = [0] * (N*M)
for r in range(N):
    for c in range(M):
        expected = 1 if (r+c)%2==0 else 0 # 좌표합에 따른 기댓값
        err = 1 if board[r*M+c]!=expected else 0 # 기댓값과 다르면 err

        left = S[r*M+c-1] if c > 0 else 0 # 왼쪽 누적합, c가 0이면 0
        up = S[(r-1)*M+c] if r > 0 else 0 # 위쪽 누적합, r이 0이면 0
        diagonal = S[(r-1)*M+c-1] if (r>0 and c>0) else 0 # r과 c가 모두 0이면 대각 누적합은 0

        S[r*M+c] = err+left+up-diagonal # 현재 좌표의 누적합=좌표의 에러유무+왼쪽 누적합+위쪽 누적합-대각 누적합

min_total = 64
for i in range(N-7):
    for k in range(M-7):
        count = 0
        # 전체 영역 (항상 존재)
        A = S[(i + 7) * M + (k + 7)]
    
        # 위쪽 여분 (i가 0보다 클 때만 존재)
        B = S[(i - 1) * M + (k + 7)] if i > 0 else 0
        
        # 왼쪽 여분 (k가 0보다 클 때만 존재)
        C = S[(i + 7) * M + (k - 1)] if k > 0 else 0
        
        # 중복 대각선 (i와 k 모두 0보다 클 때만 존재)
        D = S[(i - 1) * M + (k - 1)] if (i > 0 and k > 0) else 0
        
        # 최종 8x8 구간의 틀린 칸 개수
        count = A - B - C + D
        current_min = min(count, 64 - count)
        min_total = min(min_total, current_min)

print(min_total)