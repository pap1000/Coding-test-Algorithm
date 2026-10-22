def solution(n):
    answer = float('inf')
    for i in range(n - 1, 1, -1):
        if n % i == 1 and i < answer:
            answer = i
    return answer