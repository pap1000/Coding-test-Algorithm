T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input().split()))
    max_n = max(numbers)
    min_n = min(numbers)
    answer = max_n - min_n
    print(f"#{test_case} {answer}")