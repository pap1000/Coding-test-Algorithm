def solution(my_string):
    numbers = [int(c) for c in my_string if c in "123456789"]
    return sum(numbers)