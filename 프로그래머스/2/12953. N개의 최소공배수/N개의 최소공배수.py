def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)
        

def solution(arr):
    ans = arr[0]
    
    for num in arr[1:]:
        ans = lcm(ans, num)
    
    return ans