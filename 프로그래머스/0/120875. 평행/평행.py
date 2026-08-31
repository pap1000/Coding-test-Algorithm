from itertools import combinations

def solution(dots):
    lines = [(0, 1, 2, 3),
            (0, 2, 1, 3),
            (0, 3, 1, 2)]
    
    for l1, l2, l3, l4 in lines:
        x1, y1 = dots[l1]
        x2, y2 = dots[l2]
        x3, y3 = dots[l3]
        x4, y4 = dots[l4]
        
        if (y2-y1)/(x2-x1) == (y4-y3)/(x4-x3):
            return 1
    
    return 0