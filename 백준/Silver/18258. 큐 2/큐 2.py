import sys
from collections import deque

input = sys.stdin.readline

N_str = input().strip()
if N_str:
    N=int(N_str)
    queue = deque()

    for _ in range(N):
        command = input().split()
        if command[0] == "push":
            num = command[1]
            queue.append(num)
        elif command[0] == "pop":
            if queue:
                print(queue.popleft())
            else:
                print(-1)
        elif command[0] == "size":
            print(len(queue))
        elif command[0] == "empty":
            if queue:
                print(0)
            else:
                print(1)
        elif command[0] == "front":
            if queue:
                print(queue[0])
            else:
                print(-1)
        elif command[0] == "back":
            if queue:
                print(queue[-1])
            else:
                print(-1)