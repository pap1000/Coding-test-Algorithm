def solution(board):
    new_board = board
    max_size = 0
    if 1 in new_board[0] or 1 in [row[0] for row in board]:
        max_size = 1
    for i in range(1, len(new_board)):
        for j in range(1, len(new_board[0])):
            pr, pc, prc = new_board[i-1][j], new_board[i][j-1], new_board[i-1][j-1]
            if new_board[i][j] == 1:
                new_board[i][j] = min(pr, pc, prc) + 1
                max_size = max(max_size, new_board[i][j])
    
    return max_size**2