def solution(num_list):
    answer = []
    answer.append(sum(1 for num in num_list if num%2 == 0))
    answer.append(sum(1 for num in num_list if num%2 == 1))

    return answer