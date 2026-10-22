def solution(numbers):
    exist_n = 0
    for n in numbers:
        exist_n += int(n)
        
    return 45 - exist_n