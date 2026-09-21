def solution(N, number):
    if N == number:
        return 1
    
    dp = [set() for _ in range(9)]
    
    for k in range(1,9):
        dp[k].add(int(str(N) * k))
        
        for i in range(1, k):
            for op1 in dp[i]:
                for op2 in dp[k-i]:
                    dp[k].add(op1 + op2)
                    dp[k].add(op1 - op2)
                    dp[k].add(op1 * op2)
                    if op2 != 0:
                        dp[k].add(op1 // op2)
                        
        if number in dp[k]:
            return k

    return -1