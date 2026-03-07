import sys
import heapq

input = sys.stdin.readline
INF = float('inf')

V, E = map(int, input().split()) # vertex와 edge의 개수
K = int(input()) # 시작점
graph = [[] for _ in range(V+1)] # 각 점에 출발되는 간선을 저장할 2차원 배열

for _ in range(E): # edge를 입력
    u, v, w = map(int, input().split()) # 시작점, 도착점, 비용
    graph[u].append((v, w))

distance = [INF] * (V+1) # 최단 거리를 저장할 1차원 배열

q=[] # 방문을 관리할 큐
heapq.heappush(q, (0, K)) # 시작점을 저장
distance[K]=0 # 시작점의 거리는 0

while q:
    dist, now = heapq.heappop(q) # 큐에 저장된 거리, 현재 위치
    if distance[now] < dist: # 기존 거리가 더 짧다면 무시 
        continue

    for next_node, weight in graph[now]: # 현재 위치의 edge를 탐색
        cost = dist + weight # 비용은 현재 distance에 비용을 더함
        if cost < distance[next_node]: # 비용이 다음 노드의 distance보다 작다면 업데이트
            distance[next_node] = cost
            heapq.heappush(q, (cost, next_node)) # 큐에 다음 노드와 비용을 push

for i in range(1, V+1):
    if distance[i]==INF:
        print("INF")
    else:
        print(distance[i])
        