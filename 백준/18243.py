from collections import deque

n, k = map(int, input().split()) # n: 사람의 수, k: 친구 관계의 수
graph = [[] for _ in range(n + 1)]

for i in range(k):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

def bfs(start):
    visited = [0] * (n + 1)
    q = deque([[start, 0]])
    visited[start] = 1
    count = 1

    while q:
        now, depth = q.popleft()
        
        if depth > 6:
            return False

        for i in graph[now]:
            if not visited[i]:
                visited[i] = 1
                q.append([i, depth + 1])
                count += 1
    if count == n:
        return True
    else:
        return False

result = True
for i in range(1, n + 1):
    if not bfs(i):
        result = False

if result:
    print("Small World!")
else:
    print("Big World!")