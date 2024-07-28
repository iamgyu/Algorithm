from collections import deque

N = int(input()) # N: 컴퓨터의 수
pair = int(input()) # pair: 컴퓨터 쌍의 수(네트워크 수)
network = [[] for i in range(N + 1)]
visited = [False for i in range(N + 1)]

for i in range(pair):
    start, end = map(int, input().split())
    network[start].append(end)
    network[end].append(start)

def bfs(node):
    q = deque([node])
    visited[node] = True
    
    while q:
        now = q.popleft()

        for num in network[now]:
            if not visited[num]:
                q.append(num)
                visited[num] = True

bfs(1)
ans = 0
for i in range(N + 1):
    if visited[i]:
        ans += 1
print(ans - 1)