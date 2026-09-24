def solution(n):
    bi = list('0' + bin(n)[2:])
    
    # 뒤에서부터 '01' 패턴 탐색
    for i in range(len(bi) - 1, 0, -1):
        if bi[i - 1] == '0' and bi[i] == '1':
            bi[i - 1], bi[i] = '1', '0'
            idx = i
            break
            
    # idx 이후의 비트들을 정렬
    right_part = bi[idx:]
    right_part.sort()
    
    return int("".join(bi[:idx] + right_part), 2)