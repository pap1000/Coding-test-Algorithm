T = int(input())
for test_case in range(1, T + 1):
    n, m = list(map(int, input().split()))
    numbers = list(map(int, input().split()))
    cand = []
    
    for i in range(n - m + 1):
    	cand.append(sum(numbers[i:i+m]))
	
    print(f"#{test_case} {max(cand) - min(cand)}")