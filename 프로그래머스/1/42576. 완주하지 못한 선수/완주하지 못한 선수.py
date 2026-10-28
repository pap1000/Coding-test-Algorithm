from collections import Counter

def solution(participant, completion):
    answer = ''
    p = Counter(participant)
    c = Counter(completion)
    return list((p - c).keys()).pop()