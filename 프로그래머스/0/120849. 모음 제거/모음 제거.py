def solution(my_string):
    answer = [c for c in my_string if c not in ['a', 'e' ,'i', 'o', 'u']]
    return "".join(answer)