def solution(board):
    limit = len(board)
    danger_zone = [[0] * len(board[0]) for _ in range(limit)]
    directions = [(-1, -1), (-1, 0), (-1, 1),
                 (0, -1), (0, 0), (0, 1),
                 (1, -1), (1, 0), (1, 1)]
    
    for i, B in enumerate(board):
        for j, b in enumerate(B):
            if b == 1:
                for dr, dc in directions:
                    nr, nc = i+dr, j+dc
                    if 0 <= nr < limit and 0 <= nc < limit:
                        danger_zone[nr][nc] = 1
    
    return sum(d.count(0) for d in danger_zone)