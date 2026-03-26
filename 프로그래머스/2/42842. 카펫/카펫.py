def solution(brown, yellow):
    inner = brown - 4  # 안쪽 사각형의 둘레
    for i in range(1, int(yellow**(1/2))+1):
        # 내부 사각형 넓이가 같다면
        if i*((inner-2*i)/2) == yellow:
            return [(inner-2*i)/2+2, i+2]