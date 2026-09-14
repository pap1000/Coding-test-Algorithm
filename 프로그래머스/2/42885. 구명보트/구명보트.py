from collections import deque

def solution(people, limit):
    answer = 0
    queue = deque(sorted(people))
    
    while queue:
        if len(queue) == 1:
            queue.popleft()
            answer += 1
            continue
        if queue[-1] + queue[0] <= limit:
            queue.pop()
            queue.popleft()
            answer += 1
        else:
            queue.pop()
            answer += 1
    
    return answer