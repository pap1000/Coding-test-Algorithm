from collections import Counter

def solution(n, works):
    if n >= sum(works):
        return 0
    answer = 0
    remain = n
    works_count = Counter(works)
    prior = sorted(works_count)
    
    while remain > 0:
        curr = prior[-1]
        next_w = prior[-2] if len(prior) > 1 else 0
        curr_work = works_count[curr]
        time = (curr - next_w) * curr_work

        if time <= remain:
            remain -= time
            prior.pop()
            del works_count[curr]
            works_count[next_w] += curr_work
        else:
            q, r = divmod(remain, curr_work)
            
            del works_count[curr]
            works_count[curr - q] += curr_work - r
            works_count[curr - q -1] += r
            break
            
    
    for time, count in works_count.items():
        answer += (time ** 2) * count
        
    return answer