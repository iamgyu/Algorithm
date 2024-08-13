from collections import deque
n = int(input()) # n: 정점의 개수
graph = [[] for _ in range(n)]

for i in range(n):
    matrix = list(input().rstrip())

    for j in range(len(matrix)):
        if matrix[j] == 'Y':
            graph[i].append(j)

def bfs(start):
    count = 0
    visited = [0] * n
    q = deque([[start, 0]])
    visited[start] = 1
    
    while q:
        now, dist = q.popleft()

        if dist >= 2:
            continue

        for num in graph[now]:
            if not visited[num]:
                visited[num] = 1
                q.append([num, dist + 1])
                count += 1

    return count

ans = 0
for i in range(n):
    ans = max(ans, bfs(i))

print(ans)