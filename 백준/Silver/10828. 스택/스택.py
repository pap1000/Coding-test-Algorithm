import sys

input = sys.stdin.readline

N_str = input().strip()
if N_str:
    N=int(N_str)
    stack=[]

    for _ in range(N):
        command = input().split()
        if command[0] == "push":
            num = command[1]
            stack.append(num)
        elif command[0] == "pop":
            if stack:
                print(stack.pop())
            else:
                print(-1)
        elif command[0] == "size":
            print(len(stack))
        elif command[0] == "empty":
            if len(stack) == 0:
                print(1)
            else:
                print(0)
        elif command[0] == "top":
            if len(stack)!=0:
                print(stack[-1])
            else:
                print(-1)