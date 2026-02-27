import sys

input = sys.stdin.readline

N, M = map(int, input().split())
r, c, d = map(int, input().split())
ROOM = [list(map(int, input().split())) for _ in range(N)]

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

count = 0

while True:
    if ROOM[r][c]==0: # 현재 칸이 청소되지 않음
        ROOM[r][c] = 2
        count+=1

    look_around = False
    for i in range(4):
        d = (d+3) % 4  # 현재 바라보는 방향의 반시계로 90도
        nr, nc = r + dr[d], c + dc[d]

        if 0 <= nr < N and 0 <= nc < M and ROOM[nr][nc]==0:
            r, c = nr, nc
            look_around = True
            break

    if not look_around:
        br, bc = r - dr[d], c - dc[d]
        if 0 <= br < N and 0 <= bc < M and ROOM[br][bc]!=1:
            r, c = br, bc
        else:
            break
        
print(count)