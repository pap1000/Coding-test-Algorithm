N, K = map(int, input().split())

coins = [int(input()) for _ in range(N)]
total_count = 0

for coin in reversed(coins):
    count = 0
    count += K//coin
    K -= coin * count
    total_count += count
print(total_count)