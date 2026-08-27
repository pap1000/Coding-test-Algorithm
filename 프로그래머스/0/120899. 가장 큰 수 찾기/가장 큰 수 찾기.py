def solution(array):
    idx, max_val = max(enumerate(array), key=lambda x: x[1])
    return [max_val, idx]