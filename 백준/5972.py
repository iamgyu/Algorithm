import heapq

INF = int(1e9)

N, M = map(int, input().split()) # N: 헛간(노드), M: 길(간선)
graph = [[] for i in range(N + 1)] # 연결되어 있는 노드 정보를 담는 리스트
distance = [INF] * (N + 1)

for i in range(M):
    a, b, c = map(int, input().split()) # a: 출발 노드 , b: 도착 노드, c: 비용
    graph[a].append((b, c))
    graph[b].append((a, c))

def dijkstra():
    q = []
    heapq.heappush(q, (0, 1)) # 시작은 1번 노드부터
    distance[1] = 0

    while q:
        dist, now = heapq.heappop(q)
        
        if distance[now] < dist:
            continue
        
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra()
print(distance[N])