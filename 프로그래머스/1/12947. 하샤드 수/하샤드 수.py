def solution(x):
    X = x
    t = 0
    while X > 0:
        t += X % 10
        X //= 10
    
    return True if x % t == 0 else False