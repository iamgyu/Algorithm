T = int(input()) # 테스트 갯수

for i in range(T):
    n, d = map(int, input().split()) # n: 배열의 길이, d: 각도
    arr = []

    for i in range(n):
        arr.append(list(map(int, input().split())))

    def rotate():
        result = [[0 for _ in range(n)] for _ in range(n)]

        # task 1. 주 대각선을 가운데 열로
        for i in range(n):
            result[i][int((n + 1) / 2) - 1] = arr[i][i]

        # task 2. 가운데 열을 부 대각선으로
        for i in range(n):
            result[i][n - i - 1] = arr[i][int((n + 1) / 2) - 1]

        # task 3. 부 대각선을 가운데 행으로
        for i in range(n):
            result[int((n + 1) / 2) - 1][i] = arr[n - i - 1][i]

        # task 4. 가운데 행을 주 대각선으로
        for i in range(n):
            result[i][i] = arr[(int((n + 1) / 2) - 1)][i]

        # task 5. 다른 원소의 위치는 변하지 않음
        for i in range(n):
            for j in range(n):
                if result[i][j] == 0:
                    result[i][j] = arr[i][j]

        return result

    if d > 0:
        for i in range(d // 45):
            arr = rotate()
    else:
        for i in range((360 + d) // 45):
            arr = rotate()

    for i in range(n):
        for j in range(n):
            print(arr[i][j], end = ' ')
        print()