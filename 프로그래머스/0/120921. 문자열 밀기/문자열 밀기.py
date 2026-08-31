from collections import deque

def solution(A, B):
    A = deque(A)
    length = len(A)
    print(A)
    for i in range(length):
        if "".join(list(A)) == B:
            return i
        A.rotate(1)

    return -1