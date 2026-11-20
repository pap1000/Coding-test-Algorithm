T = int(input())

for test_case in range(1, T + 1):
    number, N = input().split()
    N = int(N)
    candidates = {number}
    length = len(number)
    
    for _ in range(N):
        next_candidates = set()
        
        for candidate in candidates:
            card = list(candidate)
            for i in range(length - 1):
                for j in range(i + 1, length):
                    card[i], card[j] = card[j], card[i]
                    
                    next_candidates.add(''.join(card))
                    
                    card[i], card[j] = card[j], card[i]
                    
        candidates = next_candidates
    
    answer = max(map(int, candidates))
    
    print(f"#{test_case} {answer}")