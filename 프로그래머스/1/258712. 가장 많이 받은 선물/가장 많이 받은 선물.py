def solution(friends, gifts):
    n = len(friends)
    name_to_id = {name: i for i, name in enumerate(friends)}
    gift_matrix = [[0] * n for _ in range(n)]
        
    for gift in gifts:
        give, take = gift.split()
        gift_matrix[name_to_id[give]][name_to_id[take]] += 1
        
    gift_scores = [sum(gift_matrix[i]) - sum(gift_matrix[k][i] for k in range(n))   for i in range(n)]

    max_gift = 0
    
    for i in range(n):
        gift_estimate = 0
        for j in range(n):
            if i == j: continue
            
            if gift_matrix[i][j] > gift_matrix[j][i]:
                gift_estimate += 1
                
            elif gift_matrix[j][i] == gift_matrix[i][j]:
                if gift_scores[i] > gift_scores[j]:
                    gift_estimate += 1
                
        max_gift = max(gift_estimate, max_gift)
    
    return max_gift