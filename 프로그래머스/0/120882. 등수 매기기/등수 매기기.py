from collections import Counter

def solution(score):
    total = [m+e for m, e in score]
    
    sorted_totals = sorted(total, reverse=True)
    
    return [sorted_totals.index(t)+1 for t in total]