# *dp 공부 반드시 필요, 문제 다시 익혀볼 것*
N, M = map(int, input().split()) # N행 M열, 행이 y, 열이 x
route = [] # 이동 경로
for i in range(N):
    route.append(list(map(int, input().split())))
    
MAX_VAL = 100 * 1000 + 1
dp = [[[MAX_VAL] * 3 for col in range(M)]for row in range(N)]

# k = 0: 오른쪽 위에서 오는거, k = 1: 중간 위에서 오는거, k = 2: 왼쪽 위에서 오는거
for i in range(N):
    if i == 0:
        for j in range(M):
            for k in range(3):
                dp[i][j][k] = route[i][j]

    else:
        for j in range(M):
            if j == 0:
                dp[i][j][0] = min(dp[i - 1][j + 1][1], dp[i - 1][j + 1][2]) + route[i][j]
                dp[i][j][1] = dp[i - 1][j][0] + route[i][j]
            elif j == M - 1:
                dp[i][j][1] = dp[i - 1][j][2] + route[i][j]
                dp[i][j][2] = min(dp[i - 1][j - 1][0], dp[i - 1][j - 1][1]) + route[i][j]
            else:
                dp[i][j][0] = min(dp[i - 1][j + 1][1], dp[i - 1][j + 1][2]) + route[i][j]
                dp[i][j][1] = min(dp[i - 1][j][0], dp[i - 1][j][2]) + route[i][j]
                dp[i][j][2] = min(dp[i - 1][j - 1][0], dp[i - 1][j - 1][1]) + route[i][j]

answer = 1e9
for i in range(M):
    answer = min(min(dp[N - 1][i]), answer)

print(answer)