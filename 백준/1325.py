from collections import deque

N, M = map(int, input().split()) # N: 컴퓨터 개수, M: 신뢰 관계 수
graph = [[] for _ in range(N + 1)]

for i in range(M):
    end, start = map(int, input().split())
    graph[start].append(end)

def bfs(node):
    q = deque([node])
    visited = [0 for _ in range(N + 1)]
    visited[node] = 1
    count = 0

    while q:
        now = q.popleft()

        for num in graph[now]:
            if not visited[num]:
                count += 1
                visited[num] = 1
                q.append(num)
    return count

ans = []
max = 0
for i in range(1, N + 1):
    result = bfs(i)
    if result > max:
        ans.clear()
        ans.append(i)
        max = result
    elif result == max:
        ans.append(i)

for i in range(len(ans)):
    print(ans[i], end = ' ')