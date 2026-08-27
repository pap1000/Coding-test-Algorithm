def solution(m, n, puddles):
    go_school = [[0]*(m+1) for _ in range(n+1)]
    go_school[1][1] = 1
    
    puddles_set = {(x,y) for x, y in puddles}
    
    for i in range(1, n+1):
        for j in range(1, m+1):
            if (i,j) == (1,1) or (j, i) in puddles_set:
                continue
            go_school[i][j] = go_school[i-1][j] + go_school[i][j-1]
            
    return go_school[n][m]%1000000007