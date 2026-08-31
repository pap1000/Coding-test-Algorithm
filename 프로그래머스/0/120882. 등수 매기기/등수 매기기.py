from collections import Counter

def solution(score):
    answer = []
    ave_score = [(m+e) for m, e in score]   # 총점과 평균 등수는 같다
    sort_score = sorted(Counter(ave_score).items(), reverse=True)
    rank_dict = {}
    i = 1
    for score, num in sort_score:
        rank_dict[score] = i
        i += num
        
    for s in ave_score:
        answer.append(rank_dict[s])
    
    return answer