T = int(input())
for test_case in range(1, T + 1):
    K, N, M = list(map(int, input().split()))
    station = list(map(int, input().split()))
    location = 0
    answer = 0
    
    while location < N - K:
        reachable = [num for num in station if location + K >= num > location]
        if not reachable:
            answer = 0
            break
        location = max(reachable)
        answer += 1
    print(f"#{test_case} {answer}")