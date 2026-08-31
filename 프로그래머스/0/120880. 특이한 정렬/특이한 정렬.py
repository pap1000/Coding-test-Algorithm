def solution(numlist, n):
    answer = []
    numlist_dic = {}
    
    for num in numlist:
        diff = abs(num-n)
        if diff not in numlist_dic:
            numlist_dic[diff] = [num]
        else:
            numlist_dic[diff].append(num)
    
    numlist_dic = {k: sorted(v, reverse=True) for k, v in sorted(numlist_dic.items())}
    
    for key in numlist_dic:
        for num in numlist_dic[key]:
            answer.append(num)
        
    return answer