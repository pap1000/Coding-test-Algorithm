from collections import Counter
def solution(s):
    return "".join(c for c, count in sorted(Counter(s).items()) if count == 1)