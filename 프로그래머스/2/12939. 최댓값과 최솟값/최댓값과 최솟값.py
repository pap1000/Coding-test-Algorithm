def solution(s):
    numlist = list(map(int, s.split()))
    big_n = max(numlist)
    small_n = min(numlist)
    
    return str(small_n) + " " + str(big_n)