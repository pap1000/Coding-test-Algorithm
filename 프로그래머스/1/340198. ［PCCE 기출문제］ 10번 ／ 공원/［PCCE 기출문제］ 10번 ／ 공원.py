def solution(mats, park):
    answer = 0
    n = len(park)
    m = len(park[0])
    
    maps = [[0] * m for _ in range(n)]
    max_size = 0
    
    for i in range(0, n):
        for j in range(0, m):
            if park[i][j] != "-1":
                continue
            elif park[i][j] == "-1" and (i == 0 or j == 0):
                maps[i][j] = 1
            else:
                left = park[i][j-1]
                up = park[i-1][j]
                diag = park[i-1][j-1]
                maps[i][j] = min(maps[i-1][j], maps[i][j-1], maps[i-1][j-1]) + 1
            max_size = max(max_size, maps[i][j])
    
    return max([size if size <= max_size else -1 for size in mats])