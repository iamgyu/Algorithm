n = int(input())
dp1 = [0 for i in range(n)]
dp2 = [0 for i in range(n)]
result_dp = [0 for i in range(n)]
a = list(map(int, input().split()))

m = max(a)

for i in range(n):
    for j in range(i):
        if a[i] > a[j] and dp1[i] < dp1[j]:
            dp1[i] = dp1[j]
    dp1[i] += 1

for i in range(n-1, -1, -1):
    for j in range(n-1, i, -1):
        if a[i] > a[j] and dp2[i] < dp2[j]:
            dp2[i] = dp2[j]
    dp2[i] += 1
    
for i in range(n):
    result_dp[i] = dp1[i] + dp2[i] - 1

print(max(result_dp))