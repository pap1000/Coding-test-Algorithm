from collections import deque

def solution(priorities, location):
    queue = [(i, prior) for i, prior in enumerate(priorities)]
    answer = 0
    
    while queue:
        curr = queue.pop(0)
        if any(curr[1] < q[1] for q in queue):  # 더 높은 우선순위가 있는 경우
            queue.append(curr)
        else:
            answer += 1
            if curr[0] == location: # 찾던 index인 경우
                return answer
    