def solution(answers):
    answer = []
    supo1 = [1, 2, 3, 4, 5]  # 5개
    supo2 = [2, 1, 2, 3, 2, 4, 2, 5]  # 8개
    supo3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]  # 10개
    
    # i번째 문제 정답
    count_1 = 0
    count_2 = 0
    count_3 = 0

    for i, a in enumerate(answers):
        if supo1[i%5] == a:
            count_1 += 1
        if supo2[i%8] == a:
            count_2 += 1
        if supo3[i%10] == a:
            count_3 += 1
    
    max_score = max([count_1, count_2, count_3])
    if max_score==count_1:
        answer.append(1)
    if max_score==count_2:
        answer.append(2)
    if max_score==count_3:
        answer.append(3)
    
    return answer