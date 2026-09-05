from collections import deque

def solution(begin, target, words):
    queue = deque([(begin, 0)])
    visited = [False] * len(words)
    
    while queue:
        curr, step = queue.popleft()
        if curr == target:
            return step
        for i, w in enumerate(words):
            if not visited[i]:
                diff = sum(c1 != c2 for c1, c2 in zip(curr, w))
                if diff == 1:
                    visited[i] = True
                    queue.append((w, step + 1))
        
    return 0