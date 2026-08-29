def solution(s):
    answer = 0
    word = s.split()
    for i, c in enumerate(word):
        if c != 'Z':
            answer += int(c)
        else:
            answer -= int(word[i-1])
    return answer