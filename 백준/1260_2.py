N, M, V = map(int, input().split()) # N: 정점의 개수, M: 간선의 개수, V: 정점의 번호
matrix = [[0 for i in range(N + 1)] for j in range(N + 1)] # 연결관계를 정리하기 위한 리스트
visited = [False for i in range(N + 1)] # 해당 노드의 방문 여부를 체크하기 위한 리스트


for i in range(M):
    node1, node2 = map(int, input().split()) # 연결되어 있는 정점 두개
    matrix[node1][node2] = matrix[node2][node1] = 1 # 연결된 경우 1로 표시

def DFS(matrix, visited, v): # 연결관계, 방문 여부, 시작 노드 받아옴
    answer = []
    stack = [] # DFS 구현을 위한 스택
    stack.append(v) # 시작 노드 추가

    while stack:
        value = stack.pop()

        if not visited[value]:
            answer.append(value)
            visited[value] = True
            
            for i in range(len(matrix[value]) - 1, -1, -1):
                if matrix[value][i] == 1 and not visited[i]:
                    stack.append(i)

    return answer

from collections import deque

def BFS(matrix, visited, v): # 연결관계, 방문 여부, 시작 노드 받아옴
    answer = []
    queue = deque() # BFS 구현을 위한 deque
    queue.append(v) # 시작 노드 추가

    while queue:
        value = queue.popleft()

        if not visited[value]:
            answer.append(value)
            visited[value] = True

            for i in range(len(matrix[value])):
                if matrix[value][i] == 1 and not visited[i]:
                    queue.append(i)
    
    return answer

    

print(*DFS(matrix, visited, V))
visited = [False for i in range(N + 1)] # 해당 노드의 방문 여부를 체크하기 위한 리스트
print(*BFS(matrix, visited, V))