def solution(N, stages):
    failure_stage = [0] * (N + 2)
    failure_rate = []
    
    for stage in stages:
        failure_stage[stage] += 1
    
    reached = len(stages)
    i = 1
    
    while i < (N + 1):
        failure = failure_stage[i]
        if reached == 0:
            failure_rate.append((0, i))
        else:
            failure_rate.append((failure/reached, i))
            reached -= failure
        i += 1
        
    failure_rate.sort(key=lambda x: (-x[0], x[1]))
    return [stage for _, stage in failure_rate]