import heapq
INF = int(1e9)

N, D = map(int, input().split()) # N: 지름길의 개수, D: 고속도로 길이
graph = [[] for _ in range(D + 1)]
distance = [INF] * (D + 1)

for i in range(D): # 거리 1로 초기화
    graph[i].append((i + 1, 1))

for i in range(N):
    start, end, length = map(int, input().split()) # 시작, 도착, 지름길 길이
    
    if end > D:
        continue
    graph[start].append((end, length))

def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0

    while queue:
        dist, node = heapq.heappop(queue)
        
        if dist > distance[node]:
            continue

        for i in graph[node]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(queue, (cost, i[0]))

dijkstra(0)
print(distance[D])