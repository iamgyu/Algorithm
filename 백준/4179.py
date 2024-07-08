from collections import deque

R, C = map(int, input().split()) # R: 미로 행의 개수, C: 미로 열의 개수
map = []
visited_j = [[-1 for _ in range(C)] for _ in range(R)]
visited_f = [[-1 for _ in range(C)] for _ in range(R)]
fire_arr = []
ans = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(R):
    temp = list(input().rstrip())
    map.append(temp)

    for j in range(C):
        if temp[j] == 'F':
            fire_arr.append((i, j))
            visited_f[i][j] = 0

if not fire_arr:
    visited_f = [[1000000 for _ in range(C)] for _ in range(R)]


def bfs_j(x, y):
    global ans

    q = deque()
    q.append((x, y))
    visited_j[x][y] = 0

    while q:
        x, y = q.popleft()

        if x == R - 1 or y == C - 1 or x == 0 or y == 0:
            ans = visited_j[x][y] + 1
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < R and 0 <= ny < C:
                if map[nx][ny] == '.' and visited_j[nx][ny] == -1 and visited_f[nx][ny] > visited_j[x][y] + 1:
                    visited_j[nx][ny] = visited_j[x][y] + 1
                    q.append((nx, ny))
                    

def bfs_f(arr):
    q = deque(arr)
    
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < R and 0 <= ny < C:
                if map[nx][ny] != '#' and visited_f[nx][ny] == -1:
                    visited_f[nx][ny] = visited_f[x][y] + 1
                    q.append((nx, ny))

bfs_f(fire_arr)

for i in range(R):
    for j in range(C):
        if map[i][j] == 'J':
            bfs_j(i, j)
            break

if not ans:
    print("IMPOSSIBLE")
else:
    print(ans)