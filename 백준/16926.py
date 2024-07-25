N, M, R = map(int, input().split()) # N: 행, M: 열, R: 회전 횟수
arr =[]
for i in range(N):
    arr.append(list(map(int, input().split())))

# 상하좌우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for i in range(R):
    move_x, move_y = M - 1, N - 1 # 이동해야 하는 x, y 길이
    x, y = 0, 0 # 배열 회전이 시작되는 x, y 좌표

    while move_x > 0 and move_y > 0:
        #하우상좌 순으로 값을 옮김
        down, right, up, left = move_y, move_x, move_y, move_x
        temp = arr[y][x] # 첫 값을 임시 저장

        while down > 0 or right > 0 or up > 0 or left > 0:
            if down > 0:
                x += dx[1]
                y += dy[1]
                down -= 1

            elif right > 0:
                x += dx[3]
                y += dy[3]
                right -= 1

            elif up > 0:
                x += dx[0]
                y += dy[0]
                up -= 1

            elif left > 0:
                x += dx[2]
                y += dy[2]
                left -= 1

            num = arr[y][x]
            arr[y][x] = temp
            temp = num

        move_x -= 2
        move_y -= 2
        x += 1
        y += 1

for i in range(N):
    for j in range(M):
        print(arr[i][j], end=' ')
    print()