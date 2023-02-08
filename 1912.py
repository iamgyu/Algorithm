n = int(input())
dp = [0 for i in range(n)]
a = list(map(int, input().split()))

dp[0] = a[0]

for i in range(1, n):
        dp[i] = max(dp[i-1] + a[i], a[i])

print(max(dp))