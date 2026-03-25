def solution(clothes):
    answer = 1
    count_part = {}
    for _, part in clothes:
        count_part[part] = count_part.get(part, 0) + 1
    for key in count_part:
        answer *= count_part[key]+1
    
    return answer-1