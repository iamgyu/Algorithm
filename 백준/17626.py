n = int(input()) # n: 숫자 입력
dp = [0, 1]

for i in range(2, n + 1):
    min_n = 4
    j = 1
    while (j ** 2) <= i:
        min_n = min(min_n, dp[i - j ** 2])
        j += 1
    dp.append(min_n + 1)

print(dp[n])