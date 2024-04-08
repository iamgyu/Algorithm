H, W, N, M = map(int, input().split())
rowMax = 0
columnMax = 0

for i in range(1, W + 1, M + 1):
    columnMax += 1

for i in range(1, H + 1, N + 1):
    rowMax += 1

print(rowMax * columnMax)