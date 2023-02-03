n = int(input())
dp = [[0 for i in range(10)] for j in range(1001)]

for i in range(0, 10):
    dp[1][i] = 1

for i in range(2, n+1):
    for j in range(0, 10):
        if j == 0:
            dp[i][j] = 0
        else:
            dp[i][j] = dp[i][j-1] + dp[i-1][j]
            
result = 0
for i in range(0, n+1):
    result += sum(dp[i])

print(result % 10007)