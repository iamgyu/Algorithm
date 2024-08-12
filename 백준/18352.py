from collections import deque
n, m, k, x = map(int, input().split()) # n: 도시의 개수, m: 도로의 개수, k: 거리 정보, x: 출발 도시
graph = [[] for _ in range(n + 1)]
visited = [-1 for _ in range(n + 1)]

for i in range(m):
    start, end = map(int, input().split())
    graph[start].append(end)

def bfs(x):
    ans = []
    q = deque([x])
    visited[x] = 0

    while q:
        now = q.popleft()

        for num in graph[now]:
            if visited[num] == -1:
                visited[num] = visited[now] + 1
                q.append(num)
    
    for i in range(len(visited)):
        if visited[i] == k:
            ans.append(i)
    
    return sorted(ans)

answer = bfs(x)
if not answer:
    print(-1)
else:
    for i in range(len(answer)):
        print(answer[i])