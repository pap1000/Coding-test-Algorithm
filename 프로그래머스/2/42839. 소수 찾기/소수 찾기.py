from itertools import permutations

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    nums = set()
    for l in range(1, len(numbers)+1): # 순열의 길이
        for p in permutations(numbers, l):  # 길이에 맞는 순열 생성
            num = int(''.join(p))  # 간격없이 합치기
            nums.add(num)
    
    answer = sum(1 for num in nums if is_prime(num))
    
    return answer