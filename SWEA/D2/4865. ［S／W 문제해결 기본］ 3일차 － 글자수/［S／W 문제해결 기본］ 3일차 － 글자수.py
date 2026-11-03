T = int(input())

for test_case in range(1, T + 1):
    c_set = set()
    str1 = input()
    str2 = input()
    max_num = 0
    
    for c in str1:
        c_set.add(c)
    
    for c in c_set:
        max_num = max(max_num, str2.count(c))
    
    print(f"#{test_case} {max_num}")