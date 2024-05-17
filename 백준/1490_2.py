from collections import deque

n, m = map(int, input().split()) # n: 세로, m: 가로
matrix = []
visited = [[-1 for i in range(m)] for j in range(n)] # 방문 여부 및 결과 저장
# 상 하 좌 우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for i in range(n):
    temp = list(map(int, input().split()))
    matrix.append(temp)

def BFS(i, j): # 시작 지점 x, y좌표 받음
    queue = deque()
    queue.append((i, j))
    visited[i][j] = 0 # 시작 지점은 값이 0

    while queue:
        x, y = queue.popleft()

        for num in range(4):
            nx = x + dx[num]
            ny = y + dy[num]

            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == -1:
                if matrix[nx][ny] == 0:
                    visited[nx][ny] = 0
                elif matrix[nx][ny] == 1:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))

for i in range(n):
    for j in range(m):
        if matrix[i][j] == 2 and visited[i][j] == -1:
            BFS(i, j)

for i in range(n):
    for j in range(m):
        if matrix[i][j] == 0:
            print(0, end=' ')
        else:
            print(visited[i][j], end=' ')
    print()