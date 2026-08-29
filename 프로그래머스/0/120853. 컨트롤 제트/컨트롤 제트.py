def solution(s):
    answer = 0
    for i, c in enumerate(s.split()):
        if c != 'Z':
            answer += int(c)
        else:
            answer -= int(s.split()[i-1])
    return answer