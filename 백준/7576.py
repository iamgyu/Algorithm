from collections import deque

M, N = map(int, input().split()) # N: 행, M: 열
storage = []

for i in range(N):
    storage.append(list(map(int, input().split())))

visited = [[-1 for _ in range(M)] for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(arr):
    q = deque(arr)


    while q:
        x, y = q.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < N and 0 <= ny < M:
                if storage[nx][ny] == 0 and visited[nx][ny] == -1:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))


# 토마토가 없는 좌표에 경우 방문 값을 0으로 설정, 익은 토마토(1)인 경우에 배열에 담아 bfs함수의 인자로 넘김
arr = []
for i in range(N):
    for j in range(M):
        if storage[i][j] == -1:
            visited[i][j] = 0
        if storage[i][j] == 1:
            arr.append((i, j))
            visited[i][j] = 0

bfs(arr)
if any(-1 in l for l in visited):
    print(-1)
else:
    print(max(map(max, visited)))