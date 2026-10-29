from collections import Counter

def solution(n, works):
    if n >= sum(works):
        return 0
    answer = 0
    remain = n
    works_count = Counter(works)
    
    while remain:
        curr = max(works_count)
        curr_work = works_count[curr]
        works_count[curr] = max(0, curr_work - remain)
        if not works_count[curr]:
            works_count.pop(curr)
        works_count[curr - 1] += min(curr_work, remain)
        remain = max(0, remain - curr_work)
    
    for time, count in works_count.items():
        for i in range(count):
            answer += time ** 2
        
    return answer