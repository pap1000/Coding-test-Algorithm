def solution(array, n):
    answer = [abs(num - n) for num in sorted(array)]
    return sorted(array)[answer.index(min(answer))]