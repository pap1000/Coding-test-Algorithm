from collections import Counter

def solution(k, tangerine):
    answer = 0
    sanggyul_tanggyul = Counter(tangerine)
    for gyul in sorted(sanggyul_tanggyul, key = lambda x : -sanggyul_tanggyul[x]):
        if k <= 0:
            break
        k -= sanggyul_tanggyul[gyul]
        answer += 1

    return answer