N = int(input()) # N * N 크기의 교실
seat = [[0 for _ in range(N)] for _ in range(N)]

# 인접한 상하좌우 체크를 위함
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# 학생들 리스트
student_list = []

# 조건 1을 위한 함수
def likeStudent(student):
    result = [] # 여러 칸 일수 있으므로 배열로 return 예정
    max = 0
    for y in range(N):
        for x in range(N):
            count = 0 # 좋아하는 학생 수를 위한 변수
            if not seat[y][x]: # 비어있을 때
                # 인접 위치 확인
                for k in range(4):
                    n_x = x + dx[k]
                    n_y = y + dy[k]

                    if 0 <= n_x < N and 0 <= n_y < N:
                        if seat[n_y][n_x] in student[1:]:
                            count += 1
            if count > max:
                result.clear()
                max = count
                result.append((x, y))
            elif count == max and not seat[y][x]:
                result.append((x, y))

    return result

def checkEmpty(condition1):
    result = [] # 비어있는 칸이 가장 많은 칸
    max = 0
    for x, y in condition1:
        count = 0
        for i in range(4):
            n_x = x + dx[i]
            n_y = y + dy[i]

            if 0 <= n_x < N and 0 <= n_y < N:
                if seat[n_y][n_x] == 0:
                    count += 1
        
        if count > max:
            result.clear()
            max = count
            result.append((x, y))
        elif count == max:
            result.append((x, y))
    
    return result


for i in range(N * N):
    student = list(map(int, input().split())) # [0]는 번호, [1],[2],[3],[4]는 좋아하는 학생의 번호
    student_list.append(student) # 만족도를 구하기 위해 학생 정보 저장

    # 조건 1. 비어있는 칸 중에서 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 자리를 정한다.
    condition1 = likeStudent(student)
    if len(condition1) == 1:
        seat[condition1[0][1]][condition1[0][0]] = student[0]
        continue
    # 조건 2. 1을 만족하는 칸이 여러 개이면, 인접한 칸 중에서 비어있는 칸이 가장 많은 칸으로 자리를 정한다.
    condition2 = checkEmpty(condition1)
    if len(condition2) == 1:
        seat[condition2[0][1]][condition2[0][0]] = student[0]
        continue
    # 조건 3. 2를 만족하는 칸도 여러 개인 경우에는 행의 번호가 가장 작은 칸으로, 그러한 칸도 여러 개이면 열의 번호가 가장 작은 칸으로 자리를 정한다.
    condition3 = sorted(condition2, key=lambda x: (x[1], x[0]))

    seat[condition3[0][1]][condition3[0][0]] = student[0]

student_list = sorted(student_list, key = lambda x: x[0]) # 학생 순번대로 정렬
# 만족도 총합 구하기
ans = 0
for i in range(N):
    for j in range(N):
        student_num = seat[i][j]
        count = 0

        for k in range(4):
            x = j + dx[k]
            y = i + dy[k]

            if 0 <= x < N and 0 <= y < N:
                if seat[y][x] in student_list[student_num - 1]:
                    count += 1
        

        if count == 1:
            ans += 1
        elif count == 2:
            ans += 10
        elif count == 3:
            ans += 100
        elif count == 4:
            ans += 1000

print(ans)