from collections import deque
n = int(input()) # n: 정점의 개수
graph = [[] for _ in range(n)]

for i in range(n):
    matrix = list(map(int, input().split()))

    for j in range(len(matrix)):
        if matrix[j] == 1:
            graph[i].append(j)

def bfs(start, end):
    visited = [0] * n
    q = deque([start])
    visited[start] = 1

    while q:
        now = q.popleft()

        for num in graph[now]:
            if num == end:
                return True
            
            else:
                if not visited[num]:
                    visited[num] = 1
                    q.append(num)
    
    return False

for i in range(n):
    temp = []
    for j in range(n):
        if bfs(i, j):
            temp.append(1)
        else:
            temp.append(0)
    print(*temp)