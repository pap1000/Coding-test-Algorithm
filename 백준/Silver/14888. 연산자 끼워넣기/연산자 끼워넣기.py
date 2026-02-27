import sys

input = sys.stdin.readline

N = int(input().strip())
NUMBERS = list(map(int, input().split()))
OP = list(map(int, input().split()))  # 0: +, 1: -, 2: *, 3: /

max_val = int(-1e9)
min_val = int(1e9)

def dfs(depth, current_total, plus, minus, multiply, divide):
    global max_val, min_val

    if depth==N:
        max_val=max(max_val, current_total)
        min_val=min(min_val, current_total)
        return

    if plus > 0:
        dfs(depth+1, current_total+NUMBERS[depth], plus-1, minus, multiply, divide)
    if minus > 0:
        dfs(depth+1, current_total-NUMBERS[depth], plus, minus-1, multiply, divide)
    if multiply > 0:
        dfs(depth+1, current_total*NUMBERS[depth], plus, minus, multiply-1, divide)
    if divide > 0:
        dfs(depth+1, int(current_total/NUMBERS[depth]), plus, minus, multiply, divide-1)
        
dfs(1, NUMBERS[0], OP[0], OP[1], OP[2], OP[3])
print(max_val)
print(min_val)