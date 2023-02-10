n = int(input())

for i in range(0, n):
    a = int(input())
    dp = [0] * (a + 4)
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4
    for k in range(4, a + 1):
        dp[k] = dp[k-1] + dp[k-2] + dp[k-3]
    
    print(dp[a])