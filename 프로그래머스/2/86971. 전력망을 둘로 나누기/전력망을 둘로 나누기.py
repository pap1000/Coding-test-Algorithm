from collections import deque

def get_count(start, n, graph):
    visited = [False] * (n+1)  # 송전탑의 방문여부
    queue = deque([start])  # 탐색할 송전탑을 저장, 처음에는 시작점
    visited[start] = True  # 시작점을 방문한 곳으로 등록
    count = 1
    
    while queue:
        curr = queue.popleft()  # 현재 탐색할 송전탑
        for neighbor in graph[curr]:  # 받아온 graph를 통해 해당 현재 송전탑에 연결된 송전탑을 탐색
            if not visited[neighbor]:  # 방문한 적이 없다면 등록 후 count
                visited[neighbor] = True
                queue.append(neighbor)
                count+=1
    return count

def solution(n, wires):
    answer = n
    for i in range(len(wires)):  # 모든 전선을 탐색
        graph = [[] for _ in range(n+1)]  # 각 송전탑에 연결된 다른 송전탑 정보를 저장할 리스트들을 생성
        for j, (u,v) in enumerate(wires):  # 각 전선의 연결점을 다른 연결점의 리스트에 저장
            if i==j: continue  # 하나의 전선을 제외
            graph[u].append(v)
            graph[v].append(u)
        g1 = get_count(1, n, graph)  # 만들어진 그래프로 하나의 그룹 내 송전탑 개수를 반환
        g2 = n-g1  # 자동으로 다른 그룹을 얻음
        answer = min(answer, abs(g1-g2))  # 두 그룹의 차

    return answer