def solution(my_string):
    expression = my_string.split()
    answer = int(expression[0])
    for i, factor in enumerate(expression):
        if factor == "+":
            answer += int(expression[i+1])
        elif factor == "-":
            answer -= int(expression[i+1])
    return answer