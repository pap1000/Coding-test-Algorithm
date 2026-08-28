def solution(age):
    digit_to_alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    return "".join([digit_to_alpha[int(c)] for c in str(age)])