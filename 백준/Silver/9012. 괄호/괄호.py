N = int(input())
for _ in range(N):
    PS = str(input())
    left_ps = 0
    right_ps = 0
    check_err = False
    for i in range(len(PS)):
        if left_ps < right_ps:
            print("NO")
            check_err = True
            break
        if PS[i]=="(":
            left_ps+=1
        elif PS[i]==")":
            right_ps+=1
    if check_err:
        continue;
    if left_ps == right_ps:
        print("YES")
    else:
        print("NO")
            