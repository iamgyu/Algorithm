from collections import deque
import heapq

INF = int(1e9)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while True:
    N = int(input())
    arr = []

    if N == 0:
        break

    for _ in range(N):
        row = list(map(int, input().split()))
        arr.append(row)
    
    queue = []
    distance = [[INF for _ in range(N)] for _ in range(N)]
    heapq.heappush(queue, (arr[0][0], 0, 0))
    distance[0][0] = arr[0][0]

    while queue:
        dist, x, y = heapq.heappop(queue)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N:
                cost = arr[nx][ny] + dist
                if cost < distance[nx][ny]:
                    distance[nx][ny] = cost
                    heapq.heappush(queue, (cost, nx, ny))

    count = 1
    print("Problem " + str(count) + ":", distance[N-1][N-1])
    count += 1