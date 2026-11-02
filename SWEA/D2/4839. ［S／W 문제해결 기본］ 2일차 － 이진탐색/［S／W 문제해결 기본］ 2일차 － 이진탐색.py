T = int(input())
for test_case in range(1, T + 1):
    P, A, B = map(int, input().split())
    al, ar = 1, P
    bl, br = 1, P
    answer = []
    while True:
        am = int((al+ar)/2)
        bm = int((bl+br)/2)
        
        if am == A:
            answer.append("A")
        else:
            if am < A:
                al = am
            else:
                ar = am
        if bm == B:
            answer.append("B")
        else:
            if bm < B:
                bl = bm
            else:
                br = bm
        if answer:
            break
                
    print(f"#{test_case} {0 if len(answer) > 1 else answer.pop()}")