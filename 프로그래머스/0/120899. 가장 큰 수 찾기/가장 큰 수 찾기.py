def solution(array):
    answer = []
    max_num = max(array)
    for i, num in enumerate(array):
        if num == max_num:
            answer.append(num)
            answer.append(i)
            return answer