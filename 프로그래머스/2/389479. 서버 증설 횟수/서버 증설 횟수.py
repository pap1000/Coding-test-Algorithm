from collections import deque

def solution(players, m, k):
    answer = 0
    players = deque(players)
    curr_player = 0
    t = 0
    t_server = [0] * 24
    
    while t < 24:
        curr_player = players.popleft()
        
        if curr_player >= (t_server[t]+1) * m:
            new_server = curr_player // m - t_server[t]
            answer += new_server
            for i in range(t, t+k):
                if i < 24:
                    t_server[i] += new_server
        t += 1
                
        
    return answer