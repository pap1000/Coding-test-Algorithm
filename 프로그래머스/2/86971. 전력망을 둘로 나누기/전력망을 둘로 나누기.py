import sys

sys.setrecursionlimit(100000)


def solution(n, wires):
    
    graph = [[] for _ in range(n+1)]
    for u, v in wires:
        graph[u].append(v)
        graph[v].append(u)
    
    visited = [False] * (n+1)
    min_diff = n
    
    def dfs(curr):
        nonlocal min_diff
        visited[curr] = True
        subtree_size = 1
        
        for neighbor in graph[curr]:
            if not visited[neighbor]:
                child_size = dfs(neighbor)
                
                diff = abs(n - 2 * child_size)
                if diff < min_diff:
                    min_diff = diff
                
                subtree_size += child_size
                
        return subtree_size
    
    dfs(1)
    
    return min_diff