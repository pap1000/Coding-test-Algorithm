T = int(input())
for test_case in range(1, T + 1):
    answer = 0
    my_str = input()
    full_str = input()
    if my_str in full_str:
        answer = 1
    print(f"#{test_case} {answer}")