def solution(s):
    answer = []
    zeros, trans = 0, 0
    
    while s != "1":  
        zeros += s.count('0')
        s = bin(len(s) - s.count('0'))[2:]
        trans += 1
    
    answer.append(trans)
    answer.append(zeros)
    
    return answer