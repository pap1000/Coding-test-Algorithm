def solution(s):
    answer = []
    s = s[2:-2].split("},{")
    tuple_set = set()
    parsed = []
    
    for nums in s:
        nums = list(map(int, nums.split(",")))
        parsed.append(nums)
    
    parsed.sort(key=len)
    
    for p in parsed:
        for num in p:
            if num not in tuple_set:
                tuple_set.add(num)
                answer.append(num)
    
    return answer