from collections import deque

N, K = map(int, input().split())
visited = [-1] * 100001

queue = deque()
queue.append((N, 0))

while queue:
    loc, cost = queue.popleft()

    if loc == K:
        print(cost)
        break

    if loc * 2 < 100001 and visited[loc * 2] == -1:
        queue.append((loc * 2, cost))
        visited[loc * 2] = 1
        
    if loc - 1 >= 0 and visited[loc - 1] == -1:
        queue.append((loc - 1, cost + 1))
        visited[loc - 1] = 1
    
    if loc + 1 < 100001 and visited[loc + 1] == -1:
        queue.append((loc + 1, cost + 1))
        visited[loc + 1] = 1