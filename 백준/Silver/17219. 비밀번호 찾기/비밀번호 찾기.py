import sys
input = sys.stdin.readline

N, M = map(int, input().split())
MY_PASSWORD = {}
for _ in range(N):
    link, password = input().split()
    MY_PASSWORD[link] = password
for _ in range(M):
    print(MY_PASSWORD[input().strip()])