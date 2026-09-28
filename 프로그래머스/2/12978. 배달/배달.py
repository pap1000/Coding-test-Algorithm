import heapq

def solution(N, road, K):
    graph = [[] for _ in range(N + 1)]
    
    # 인접 리스트
    for u, v, w in road:
        graph[u].append((v, w))
        graph[v].append((u, w))
    
    INF = float('inf')
    distances = [INF] * (N + 1)
    distances[1] = 0
    # 현재까지의 거리, 현재 노드
    q = [(0, 1)]
    
    while q:
        current_dist, current_node =  heapq.heappop(q)
        
        if current_dist > distances[current_node]:
            continue
        
        # 현재 current_dist가 기존 거리보다 짧은 경우 업데이트
        for neighbor, weight in graph[current_node]:
            distance = current_dist + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(q, (distance, neighbor))
                
    return sum(1 for dist in distances[1:] if dist <= K)