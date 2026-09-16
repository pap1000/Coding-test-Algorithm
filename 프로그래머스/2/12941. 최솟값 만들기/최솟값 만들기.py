from collections import deque

def solution(A,B):
    answer = 0
    new_A = deque(sorted(A))
    new_B = deque(sorted(B))
    
    for i in range(len(A)):
        answer += new_A.pop() * new_B.popleft()

    return answer