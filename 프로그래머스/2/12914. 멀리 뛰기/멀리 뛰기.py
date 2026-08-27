def solution(n):
    do_flip = [0] * (n+1)
    do_flip[0] = 1
    do_flip[1] = 1
    
    if n>=2:
        for i in range(2, n+1):
            do_flip[i] = (do_flip[i-1] + do_flip[i-2])
    
    
    return do_flip[n]%1234567