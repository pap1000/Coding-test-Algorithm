N, M = map(int, input().split())

No_listen = set(input() for _ in range(N))
No_seen = set(input() for _ in range(M))
No_listen_and_seen = sorted(No_listen & No_seen)

print(len(No_listen_and_seen))
print(*No_listen_and_seen, sep="\n")