def solution(arr, divisor):
    answer = []
    
    for num in sorted(arr):
        if num % divisor == 0:
            answer.append(num)
    return answer if answer else [-1]