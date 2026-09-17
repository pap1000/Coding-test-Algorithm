def solution(n):
    if n <= 2:
        return 1
    
    answer = 1
    
    for i in range(1, n//2+2):
        numlist = []
        num = i
        
        while sum(numlist) < n:
            numlist.append(num)
            num += 1
            
        if sum(numlist) == n:
            answer += 1
            
    return answer