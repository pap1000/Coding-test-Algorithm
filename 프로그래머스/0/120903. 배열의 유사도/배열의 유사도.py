def solution(s1, s2):
    answer = 0
    dictionary = set()
    for s in s1:
        dictionary.add(s)
    for s in s2:
        if s in dictionary:
            answer += 1
    return answer