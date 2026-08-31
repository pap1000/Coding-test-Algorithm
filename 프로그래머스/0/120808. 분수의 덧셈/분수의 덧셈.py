import math

def solution(numer1, denom1, numer2, denom2):
    total_numer = numer1 * denom2 + numer2 * denom1
    total_denom = denom1 * denom2
    gcd = math.gcd(total_numer, total_denom)
    
    return [total_numer//gcd, total_denom//gcd]