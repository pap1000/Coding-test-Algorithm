def solution(numbers, target):
    def dfs(index, curr_sum):
        if index == len(numbers):
            return 1 if curr_sum == target else 0
        return dfs(index+1, curr_sum+numbers[index]) + dfs(index+1, curr_sum-numbers[index])
    return dfs(0, 0)