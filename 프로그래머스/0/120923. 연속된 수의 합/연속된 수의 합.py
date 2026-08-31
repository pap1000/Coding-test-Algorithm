def solution(num, total):
    answer = []
    middle = total//num
    if num%2 == 0:
        for i in range(middle-(num//2)+1, middle+(num//2)+1):
            answer.append(i)
    else:
        for i in range(middle-(num//2), middle+(num//2)+1):
            answer.append(i)
            
    return answer