from collections import defaultdict

def solution(clothes):
    answer = 1
    category = defaultdict(list)
    for clothe, part in clothes:
        category[part].append(clothe)
    
    for cate in category:
        answer *= (len(category[cate]) + 1)
        
    return answer - 1