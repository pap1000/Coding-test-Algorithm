def solution(n):
    answer = [[]]
    def dfs(n, start, via, end):
        if n == 1:
            return [[start, end]]
        else:
            return dfs(n-1, start, end, via) + [[start, end]] + dfs(n-1, via, start, end)
    return dfs(n, 1, 2, 3)