def solution(before, after):
    for c1 in before:
        if before.count(c1) != after.count(c1):
            return 0
    return 1