def solution(lines):
    sets = [set(range(start, end)) for start, end in lines]
    return len((sets[0] & sets[1]) | (sets[1] & sets[2]) | (sets[0] & sets[2]))