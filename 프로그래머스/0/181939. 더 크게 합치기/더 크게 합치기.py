def solution(a, b):
    answer = 0
    n1 = str(a)+str(b)
    n2 = str(b)+str(a)
    answer = max(n1, n2)
    return int(answer)