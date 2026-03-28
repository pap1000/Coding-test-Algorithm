def solution(arr):
    answer = []
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    x_num = -1
    for num in arr:
        if num!=x_num:
            answer.append(num)
            x_num=num
    return answer