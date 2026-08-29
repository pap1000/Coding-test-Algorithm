def solution(i, j, k):
    answer = 0
    K = str(k)
    for i in range(i, j+1):
        for c in str(i):
            if c == K:
                answer+=1
    return answer