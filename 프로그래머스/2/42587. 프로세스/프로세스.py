from collections import deque

def solution(priorities, location):
    q1 = deque([(i, prior) for i, prior in enumerate(priorities)])
    q2 = deque(sorted(priorities, reverse=True))
    count = 0
    
    while(q1):
        if q1[0][1] == q2[0]:
            count += 1
            idx, _ = q1.popleft()
            q2.popleft()
            if idx == location:
                return count
        else:
            q1.append(q1.popleft())