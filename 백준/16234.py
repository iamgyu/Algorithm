from collections import deque

N, L, R = map(int, input().split())
arr = [] # 입력받는 배열
answer = 0  # 정답

for i in range(N):
    people = list(map(int, input().split()))
    arr.append(people)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(i, j):
    queue = deque()
    union = []
    queue.append((i, j))
    union.append((i, j))

    while queue:
        x, y = queue.popleft()

        for num in range(4):
            nx = x + dx[num]
            ny = y + dy[num]

            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
                if L <= abs(arr[nx][ny] - arr[x][y]) <= R:
                    visited[nx][ny] = 1
                    queue.append((nx, ny))
                    union.append((nx, ny))

    return union

while True:
    visited = [[0 for _ in range(N)] for _ in range(N)]
    flag = False

    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                visited[i][j] = 1
                country = bfs(i, j)

                if len(country) > 1:
                    flag = True
                    people = sum(arr[x][y] for x, y in country) // len(country)
                    for x, y in country:
                        arr[x][y] = people

    if not flag:
        break
    
    answer += 1

print(answer)