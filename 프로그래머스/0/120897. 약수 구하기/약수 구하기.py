def solution(n):
    answer = []
    for i in range(1, int(n**(1/2))+1):
        if i**2 == n:
            answer.append(i)
            continue
        if n % i == 0:
            answer.append(i)
            answer.append(n//i)
            
    return sorted(answer)