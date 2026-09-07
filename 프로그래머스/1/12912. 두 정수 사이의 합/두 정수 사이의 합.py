def solution(a, b):
    if a == b:
        return a
    
    return (a+b) * (abs(b-a)+1)/2