def solution(nums):
    answer = 0
    pukimon = {}
    for num in nums:
        pukimon[num] = pukimon.get(num, 0) + 1
    answer = min(len(pukimon), len(nums)/2)
    return answer