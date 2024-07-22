N = int(input()) # N: N * N 크기
find = int(input()) # 좌표가 궁금한 숫자
arr = [[0] * N for _ in range(N)] # 결과 그래프

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

x, y = N // 2, N // 2 # 중심 좌표
arr[x][y] = 1 # 시작 좌표 추가

# 시작 번호
num = 2
# 첫 외각 크기
size = 3

while x != 0 or y != 0:

    while(num <= size * size):
        if(x == y == (N // 2)):
            up, right, down, left = size, size - 2, size - 1, size - 1
            x += dx[0]
            y += dy[0]
            up -= 1
        # 상우하좌상 순서로 이동
        elif right > 0:
            x += dx[3]
            y += dy[3]
            right -= 1
        elif down > 0:
            x += dx[1]
            y += dy[1]
            down -=1
        elif left > 0:
            x += dx[2]
            y += dy[2]
            left -= 1
        else:
            x += dx[0]
            y += dy[0]
            up -= 1

        arr[x][y] = num
        num += 1

    size += 2
    N -= 2

find_x, find_y = -1, -1

for i in range(len(arr)):
    for j in range(len(arr)):
        if arr[i][j] == find:
            find_x, find_y = i + 1, j + 1
        print(arr[i][j], end = ' ')
    print()

print(find_x, find_y)