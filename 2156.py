n = int(input())

dp = [0] * 10000
p = [0] * 10000

for i in range(0, n):
    p[i] = int(input())

dp[0] = p[0]
dp[1] = p[0] + p[1]
dp[2] = max(dp[0] + p[2], p[1] + p[2], dp[1])

for i in range(3, n):
    dp[i] = max(dp[i-2] + p[i], dp[i-3] + p[i-1] + p[i], dp[i-1])
    
print(dp[n-1])