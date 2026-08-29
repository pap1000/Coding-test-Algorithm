def solution(bin1, bin2):
    answer = ''
    length1 = len(bin1)
    length2 = len(bin2)
    total = sum(int(b1) * (2**(length1-i-1)) for i, b1 in enumerate(bin1)) + sum(int(b2) * (2**(length2-i-1)) for i, b2 in enumerate(bin2))
    
    if total == 0:
        return "0"
    
    while(total>0):
        answer += str(total%2)
        total //= 2
    
    return answer[::-1]