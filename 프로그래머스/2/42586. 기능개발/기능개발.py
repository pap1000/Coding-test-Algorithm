from collections import deque

def solution(progresses, speeds):
    answer = []
    queue = deque(progresses)
    queue2 = deque(speeds)
    
    while(queue):
        for i in range(len(queue)):
            queue[i]+=queue2[i]
        if queue[0] >= 100:  # 큐의 1순위가 진행률이 100 이상
            count = 0
            while queue and queue[0]>=100:
                queue.popleft()
                queue2.popleft()
                count+=1  # 배포되는 기능 수
            answer.append(count)
    return answer