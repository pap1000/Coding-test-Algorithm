def solution(n):
    answer = 0
    for i in range(1, int(n**(1/2))+1):
        if i ** 2 == n:
            answer += i
        elif n % i == 0:
            answer += i + (n//i)
    return answer