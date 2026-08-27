def solution(triangle):
    for i in reversed(range(0, len(triangle))):
        for j in range(0, i):
            triangle[i-1][j] = max(triangle[i][j]+triangle[i-1][j], triangle[i][j+1]+triangle[i-1][j])
    return triangle[0][0]