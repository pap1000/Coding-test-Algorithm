def solution(players, callings):
    position = {
        player: rank
        for rank, player in enumerate(players)
    }
    
    for player in callings:
        rank = position[player]
        front_player = players[rank -1]
        
        players[rank - 1], players[rank] = player, front_player
        position[player] = rank - 1
        position[front_player] = rank
        
    return players