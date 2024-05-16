from collections import deque

n, m = map(int, input().split()) # n: 세로, m: 가로
matrix = [] # 입력받는 지도
visited = [[-1 for i in range(m)] for j in range(n)] # 결과 및 방문 여부를 확인 하기 위한 리스트

# 상 하 좌 우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for i in range(n):
    arr = list(map(int, input().split()))
    matrix.append(arr)

def bfs(i, j):
    queue = deque()
    queue.append((i, j))
    visited[i][j] = 0
    while queue:
        x, y = queue.popleft()

        for num in range(4):
            nx, ny = x + dx[num], y + dy[num]

            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == -1:
                if matrix[nx][ny] == 0:
                    visited[nx][ny] = 0
                elif matrix[nx][ny] == 1:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))


for i in range(n):
    for j in range(m):
        if matrix[i][j] == 2 and visited[i][j] == -1:
            bfs(i,j)

for i in range(n):
    for j in range(m):
        if matrix[i][j] == 0:
            print(0, end=' ')
        else:
            print(visited[i][j], end=' ')
    print()