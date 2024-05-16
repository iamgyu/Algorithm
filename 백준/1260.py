	
from collections import deque

N, M, V = map(int, input().split()) # N: 정점의 개수, M: 간선의 개수, V: 탐색을 시작할 정점의 번호
matrix = [[0 for i in range(N + 1)] for j in range(N + 1)] # 연결관계를 저장하기 위한 리스트
visited = [False for i in range(N + 1)] # 방문을 했는지 확인하기 위한 리스트

for i in range(M):
    v1, v2 = map(int, input().split()) # 연결된 정점 두개 입력 받음
    matrix[v1][v2] = matrix[v2][v1] = 1 # 서로 연결이 되어 있는 경우 1로 변환

def DFS(matrix, visited, v):
    stack = [] # 결과 도출을 위한 stack 리스트
    stack.append(v) # 탐색 시작 정점 번호 추가
    answer = []

    while stack:
        value = stack.pop()
        if not visited[value]:
            answer.append(value)
            visited[value] = True
            
        for i in range(len(matrix[value]) - 1, -1, -1):
             if matrix[value][i] == 1 and not visited[i]:
                stack.append(i)
    
    return answer

print(*DFS(matrix, visited, V))
visited = [False for i in range(N + 1)] # 방문을 했는지 확인하기 위한 리스트

def BFS(matrix, visited, v):
    queue = deque() # 결과 도출을 위한 deque
    queue.append(v) # 탐색 시작 정점 번호 추가
    answer = []

    while queue:
        value = queue.popleft()
        if not visited[value]:
            answer.append(value)
            visited[value] = True
        
        for i in range(len(matrix[value])):
            if matrix[value][i] == 1 and not visited[i]:
                queue.append(i)

    return answer

print(*BFS(matrix, visited, V))