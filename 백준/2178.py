from collections import deque
N, M = map(int, input().split())
maze = []

# 1은 이동 가능, 0은 이동 불가능
for i in range(N):
    maze.append(list(map(int, input().rstrip())))

visited = [[0 for _ in range(M)] for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    q = deque([(0, 0)])
    visited[0][0] = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if maze[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))

bfs()
print(visited[N - 1][M - 1])