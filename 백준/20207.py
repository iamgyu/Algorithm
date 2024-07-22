N = int(input()) # N: 일정 갯수
calendar = [0] * 366

for i in range(N):
    start, end = map(int, input().split())

    for j in range(start, end + 1):
        calendar[j] += 1

width = 0
height = 0
ans = 0

for i in range(366):
    if calendar[i] != 0:
        height = max(height, calendar[i])
        width += 1
    else:
        ans += height * width
        width = 0
        height = 0

ans += height * width
print(ans)