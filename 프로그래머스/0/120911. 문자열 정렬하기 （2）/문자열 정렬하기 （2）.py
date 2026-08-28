def solution(my_string):
    return "".join(sorted(list([c for c in my_string.lower()])))