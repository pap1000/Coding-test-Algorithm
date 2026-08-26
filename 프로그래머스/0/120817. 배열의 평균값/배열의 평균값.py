def solution(numbers):
    total = 0
    total = sum(num for num in numbers)
    return total/len(numbers)