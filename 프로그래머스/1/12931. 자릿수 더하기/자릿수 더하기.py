def solution(n):
    answer = 0
    N = n

    while N:
        answer += N%10
        N //= 10
   
    return answer