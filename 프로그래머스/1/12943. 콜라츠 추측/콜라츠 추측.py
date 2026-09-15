def solution(num):
    answer = 0
    n = num
    
    while n!=1:
        if n % 2 == 0:
            n //= 2
            answer += 1
        else:
            n = 3 * n + 1
            answer += 1
            
    return answer if answer <= 500 else -1