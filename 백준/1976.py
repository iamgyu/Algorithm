from collections import deque

def bfs(start):
    queue = deque()
    queue.append(start)
    visited[start] = 1

    while queue:
        now = queue.popleft()
        
        for i in range(N):
            if graph[now][i] == 1 and visited[i] == 0:
                visited[i] = 1
                queue.append(i)

N = int(input()) # 도시의 수
M = int(input()) # 여행계획의 도시의 수
graph = []

for i in range(N):
    arr = list(map(int, input().split()))
    graph.append(arr)

plan = list(map(int, input().split()))

visited = [0] * (N + 1)
result = "YES"
bfs(plan[0] - 1)

for p in plan:
    if visited[p - 1] == 0:
        result = "NO"
        break

print(result)