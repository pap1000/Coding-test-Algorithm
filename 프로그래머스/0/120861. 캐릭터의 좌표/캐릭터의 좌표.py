def solution(keyinput, board):
    move = {"left": (-1, 0), "right": (1, 0), "up": (0, 1), "down": (0, -1)}
    
    x_limit = board[0] // 2
    y_limit = board[1] // 2
    
    x, y = 0, 0
    for key in keyinput:
        dx, dy = move[key]
        
        x = max(-x_limit, min(x+dx, x_limit))
        y = max(-y_limit, min(y+dy, y_limit))
    
    return [x, y]