n, m, k = map(int, input().split())

def search(x, y):
    dp = [[0 for _ in range(y + 1)] for _ in range(x + 1)]

    for i in range(1, x + 1):
        for j in range(1, y + 1):
            if i == 1 and j == 1:
                dp[i][j] = 1
                continue
            
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    return dp[x][y]

if k == 0:
    print(search(n, m))
else:
    dotN1 = (k - 1) // m + 1
    dotM1 = k - (dotN1 - 1) * m
    dotN2 = n - (dotN1 - 1)
    dotM2 = m - (dotM1 - 1)

    r1 = search(dotN1, dotM1)
    r2 = search(dotN2, dotM2)

    print(r1 * r2)