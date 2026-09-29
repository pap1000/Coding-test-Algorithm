import heapq

def dijkstra(start_node, n, graph):
    INF = float('inf')
    dist = [INF] * (n + 1)
    
    dist[start_node] = 0
    pq = [(0, start_node)]
    
    while pq:
        current_dist, current_node = heapq.heappop(pq)
        
        if dist[current_node] < current_dist:
            continue
        
        for neighbor, weight in graph[current_node]:
            new_dist = current_dist + weight
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))
    
    return dist
        

def solution(n, s, a, b, fares):
    graph = [[] for _ in range(n + 1)]
    
    for u, v, w in fares:
        graph[u].append((v, w))
        graph[v].append((u, w))
    
    dist_s = dijkstra(s, n, graph)
    dist_a = dijkstra(a, n, graph)
    dist_b = dijkstra(b, n, graph)
    
    min_cost = float('inf')
    
    for k in range(1, n + 1):
        total = dist_s[k] + dist_a[k] + dist_b[k]
        if total < min_cost:
            min_cost = total
    
    return min_cost