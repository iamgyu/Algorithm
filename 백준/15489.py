r, c, w = map(int, input().split()) # r 번째 줄, c번째 숫자, w변의 수


def pascal_triangle():
    arr = [[1], [1, 1]]

    for i in range(2, 30):
        temp = []
        temp.append(1)
        for j in range(1, i):
            temp.append(arr[i - 1][j - 1] + arr[i - 1][j])
        temp.append(1)
        arr.append(temp)

    return arr

ans_arr = pascal_triangle()
ans = 0
temp_num = 1 # 삼각형 꼭지점부터 w까지 커지는 숫자

for i in range(r - 1, r - 1 + w):
    for j in range(temp_num):
        ans += ans_arr[i][c + j - 1]
    temp_num += 1

print(ans)