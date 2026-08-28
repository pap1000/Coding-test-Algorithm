def solution(my_string, num1, num2):
    answer = ''
    temp1 = my_string[num1]
    temp2 = my_string[num2]
    
    for i, c in enumerate(my_string):
        if i == num1:
            answer+=temp2
        elif i == num2:
            answer+=temp1
        else:
            answer+=c
    return answer