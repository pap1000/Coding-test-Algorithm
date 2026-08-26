def solution(n):
    answer = 0
    dp = [0]*(n+1)
    dp[0] = 1
    dp[2] = 3
    for i in range(4, n+1):
        if i%2 == 1:
            dp[i] = 0
            continue
        dp[i] = 4*dp[i-2] - dp[i-4]
    answer = dp[n]%1000000007
    return answer