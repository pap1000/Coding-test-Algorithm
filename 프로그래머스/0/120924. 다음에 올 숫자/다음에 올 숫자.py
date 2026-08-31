def solution(common):
    a1, a2, a3 = common[:3]
    
    if a2 - a1 == a3 - a2:
        return common[-1] + (a2-a1)
    else:
        return common[-1] * (a2//a1)