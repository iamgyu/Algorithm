n = int(input()) # n: 남은 날짜
table = []
for i in range(n):
    t, p = map(int, input().split()) # t: 걸리는 기간, p: 금액
    table.append([t, p])

dp = [0 for _ in range(n + 1)]

for i in range(n - 1, -1, -1):
    if i + table[i][0] > n:
        dp[i] = dp[i + 1]
    else:
        dp[i] = max(dp[i + 1], dp[i + table[i][0]] + table[i][1])

print(dp[0])