n = int(input())
candy = [list(input()) for _ in range(n)]

def checkMaxNum():
    max_n = 1
    # 가로 체크
    for i in range(n):
        count = 1
        for j in range(1, n):
            if candy[i][j] == candy[i][j - 1]:
                count += 1
            else:
                count = 1
            max_n = max(max_n, count)
    
    # 세로 체크
    for i in range(n):
        count = 1
        for j in range(1, n):
            if candy[j][i] == candy[j - 1][i]:
                count += 1
            else:
                count = 1
            max_n = max(max_n, count)
    
    return max_n

result = 1
for i in range(n):
    for j in range(n - 1):
        if j + 1 < n and candy[i][j] != candy[i][j + 1]:
            candy[i][j], candy[i][j + 1] = candy[i][j + 1], candy[i][j]
            result = max(result, checkMaxNum())
            candy[i][j], candy[i][j + 1] = candy[i][j + 1], candy[i][j]

        if i + 1 < n and candy[i][j] != candy[i + 1][j]:
            candy[i][j], candy[i + 1][j] = candy[i + 1][j], candy[i][j]
            result = max(result, checkMaxNum())
            candy[i][j], candy[i + 1][j] = candy[i + 1][j], candy[i][j]

print(result)