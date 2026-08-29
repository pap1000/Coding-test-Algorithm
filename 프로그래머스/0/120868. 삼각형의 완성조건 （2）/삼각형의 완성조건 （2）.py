def solution(sides):
    max_side = max(sides)
    min_side = min(sides)
    return (max_side+min_side) - (max_side-min_side) - 1