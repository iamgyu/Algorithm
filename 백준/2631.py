N = int(input()) # 학생 수
arr = [int(input()) for _ in range(N)] # 학생들 위치 배열
dp = [0 for i in range(N)]
dp[0] = 1
max_num = 0

for i in range(1, N):
    for j in range(0, i):
        if arr[i] > arr[j]:
            max_num = max(max_num, dp[j])
    dp[i] = max_num + 1
    max_num = 0

print(N - max(dp))