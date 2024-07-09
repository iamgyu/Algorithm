import heapq
INF = 1e9
N, M, X = map(int, input().split()) # N: 마을의 수, M: 단방향 도로 개수, X: 파티가 열리는 마을 번호
graph = [[] for _ in range(N + 1)]
total_distance = [0 for _ in range(N + 1)]

for i in range(M):
    s, e, d = map(int, input().split()) # s: start노드, e: end노드, d: 비용(거리)
    graph[s].append((e, d)) # 시작노드에 도착노드와 비용 삽입

def dijkstra(start):
    q = []
    distance = [INF] * (N + 1)
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            if dist + i[1] < distance[i[0]]:
                distance[i[0]] = dist + i[1]
                heapq.heappush(q, (dist + i[1], i[0]))
    
    if start != X:
        total_distance[start] += distance[X]
    else:
        for i in range(1, N + 1):
            if i != X:
                total_distance[i] += distance[i]

for i in range(1, N + 1):
    dijkstra(i)

print(max(total_distance))