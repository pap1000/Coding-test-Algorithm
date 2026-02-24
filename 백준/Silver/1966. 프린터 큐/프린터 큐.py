from collections import deque

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    priorities = list(map(int, input().split()))
    queue = deque(enumerate(priorities))

    count = 0
    
    while queue:
        front = queue.popleft()
        if any(front[1] < doc[1] for doc in queue):  # 큐의 문서 중 어떤 문서라도 중요도가 더 높은 경우
            queue.append(front)
        else:  # front가 가장 중요도가 높거나 같은 경우
            count+=1
            if front[0]==M:
                print(count)
                break
            