def solution(my_str, n):
    answer = []
    i = 0
    length = len(my_str)
    for i in range(0, length, n):
        answer.append(my_str[i: i+n])
        
    return answer