R, C = map(int, input().split()) # R: 세로, C: 가로
graph = []
alphabet = set()
answer = 1

for i in range(R):
    temp = list(input())
    graph.append(temp)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, count):
    global answer
    answer = max(answer, count)

    for num in range(4):
        nx = x + dx[num]
        ny = y + dy[num]

        if 0 <= nx < R and 0 <= ny < C and graph[nx][ny] not in alphabet:
            alphabet.add(graph[nx][ny])
            dfs(nx, ny, count + 1)
            alphabet.remove(graph[nx][ny])


alphabet.add(graph[0][0])
dfs(0, 0, 1)
print(answer)