N, M = map(int, input().split())
NUMBERS = [0] * N
min_diff = int(2e9)
start = 0
end = 0

for i in range(N):
    NUMBERS[i] = int(input())
NUMBERS.sort()

while end<N:
    diff = NUMBERS[end]-NUMBERS[start]
    if diff < M:
        end+=1
    else:
        min_diff = min(min_diff, diff)
        start += 1
        if start > end:
            end = start

print(min_diff)