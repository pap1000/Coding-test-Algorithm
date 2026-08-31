from collections import Counter

def solution(array):
    num_count = Counter(array)
    answer = num_count.most_common(2)
    
    if len(answer) == 1:
        return answer[0][0]
    
    if answer[0][1] == answer[1][1]:
        return -1
    
    else:
        return answer[0][0]