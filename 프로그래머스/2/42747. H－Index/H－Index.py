def solution(citations):
    citations = sorted(citations)
    n = len(citations)
    for i in range(n):
        if citations[i] >= n-i:  # 최대 h 구하기
            return n-i
    return 0