from itertools import combinations

T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    nums = [i for i in range(1, 13)]
    answer = 0
    
    for c in combinations(nums, N):
        if sum(c) == K:
            answer += 1
                
    print(f"#{test_case} {answer}")