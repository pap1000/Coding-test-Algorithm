def gcd(m, n):
    while(n):
        m, n = n, m % n
    return m

def solution(a, b):    
    print(a, b)
    div = gcd(a, b)
    b //= div
    
    while b%5 == 0:
        b = b / 5
    while b%2 == 0:
        b = b / 2
    if b != 1:
        return 2
            
    return 1