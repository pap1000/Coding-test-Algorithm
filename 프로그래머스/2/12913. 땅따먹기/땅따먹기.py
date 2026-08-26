def solution(land):
    answer = 0

    sum_table = land
    for i in range(1, len(sum_table)):  # 행번호
        for j in range(4):  # 현재 테이블 열번호
            origin = sum_table[i][j]
            max_prev = 0
            for k in range(4):  # 이전 테이블 열번호
                if j!=k:
                    max_prev = max(sum_table[i-1][k]+origin, max_prev)
                    sum_table[i][j] = max_prev
                    
    return max(*sum_table[-1])