def solution(n):
    answer = 0
    for i in range(1, n+1):
        factors = 0
        for j in range(1, int(i**(1/2)+1)):
            if i%j == 0:
                factors += 1
        if factors > 1:
            answer+=1
        else:
            continue
            
    return answer