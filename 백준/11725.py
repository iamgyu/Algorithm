from collections import deque
N = int(input()) # N: 노드의 개수
graph = [[] for _ in range(N + 1)]

for i in range(N - 1):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

def bfs(node):
    result = [0 for _ in range(N + 1)]
    q = deque([node])

    while q:
        now = q.popleft()
        for num in graph[now]:
            if result[num] == 0:
                result[num] = now
                q.append(num)

    return result

result = bfs(1)
for i in range(2, len(result)):
    print(result[i])