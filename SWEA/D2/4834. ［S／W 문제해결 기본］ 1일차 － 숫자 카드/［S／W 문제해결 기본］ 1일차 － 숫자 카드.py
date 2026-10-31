T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    length = int(input())
    card = int(input())
    count = [0] * 10
    
    for i in range(length):
        num = card % 10
        card //= 10
        count[num] += 1
    
    max_num = max(count)
    cand = [i for i, num in enumerate(count) if num == max_num]
    answer = max(cand)
    print(f"#{test_case} {answer} {count[answer]}")