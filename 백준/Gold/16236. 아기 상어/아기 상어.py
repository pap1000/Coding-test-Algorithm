import collections

def solve():
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]

    r, c = 0, 0
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 9:
                r, c = i, j
                grid[i][j]=0

    size = 2
    ate = 0
    total_time = 0

    while True:
        queue = collections.deque([(r, c, 0)])
        visited = [[False]*N for _ in range(N)]
        visited[r][c] = True

        candidates = []
        min_dist = float('inf')

        while queue:
            curr_r, curr_c, dist = queue.popleft()
            if dist >= min_dist:
                continue
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = curr_r + dr, curr_c + dc

                if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]: # 유효한 좌표값이면서 방문한 적 없을 시
                    if grid[nr][nc] <= size: # 이동가능한다면
                        visited[nr][nc] = True
                        if 0 < grid[nr][nc] < size: # 먹을 수 있는 사이즈
                            candidates.append((dist+1, nr, nc))
                            min_dist = dist+1
                        else: # 먹을 수 없는 사이즈
                            queue.append((nr, nc, dist+1))

        if not candidates: # 먹을 물고기가 없다면 종료
            break

        candidates.sort()
        d, next_r, next_c = candidates[0]

        total_time += d
        grid[next_r][next_c] = 0
        r, c = next_r, next_c
        ate += 1
        if ate == size:
            size+=1
            ate=0
    print(total_time)
solve()