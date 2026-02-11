N = int(input())
arr = [int(input()) for _ in range(N)]
new_arr = sorted(arr)

for num in new_arr:
    print(num)