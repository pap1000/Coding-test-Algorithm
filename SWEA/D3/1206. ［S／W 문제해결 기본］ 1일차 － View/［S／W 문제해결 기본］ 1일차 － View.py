T = 10
for test_case in range(1, T + 1):
    answer = 0
    length = int(input())
    buildings = list(map(int, input().split()))

    for i in range(2, length - 2):
        left = max(buildings[i - 1],  buildings[i - 2])
        right = max(buildings[i + 1],  buildings[i + 2])
        curr = buildings[i]
        answer += max(min(curr - left, curr - right), 0)
    
    print(f"#{test_case} {answer}")