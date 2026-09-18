from collections import deque

def solution(prices):
    answer = []
    p = deque(prices)
    
    while p:
        curr = p.popleft()
        t = len(p)
        
        for i, next_p in enumerate(p):
            if curr > next_p:
                t = i+1
                break
                
        answer.append(t)

    
    return answer