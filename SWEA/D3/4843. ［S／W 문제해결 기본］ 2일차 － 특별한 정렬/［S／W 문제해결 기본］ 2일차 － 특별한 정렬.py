from collections import deque

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [0] * 10
    numbers = deque(sorted(map(int, input().split())))
    for i in range(10):
        if i % 2 == 0:
            arr[i] = numbers.pop()
        else:
            arr[i] = numbers.popleft()
    answer = " ".join(map(str, arr))
    print(f"#{test_case} {answer}")