from collections import deque

def solution(elements):
    seq = deque(elements)
    L = len(seq)
    num_dic = set()
    
    for i in range(1,L + 1):    # 부분 수열 길이
        for j in range(0, L):   # 회전 길이
            seq.rotate(1)
            num_dic.add(sum(list(seq)[:i]))
    return len(num_dic)