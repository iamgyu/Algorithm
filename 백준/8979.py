N, nation = map(int, input().split())

arr = [[0 for col in range(4)] for row in range(N)]

for i in range(N):
    arr[i][0], arr[i][1], arr[i][2], arr[i][3] = map(int, input().split())

arr.sort(key=lambda x: (-x[1], -x[2], -x[3]))

answer = 0
nation_gold = 0
nation_silver = 0
nation_bronze = 0

for i in range(N):
    if arr[i][0] == nation:
        answer, nation_gold, nation_silver, nation_bronze = i + 1, arr[i][1], arr[i][2], arr[i][3]

for i in range(N):
    if arr[i][1] == nation_gold and arr[i][2] == nation_silver and arr[i][3] == nation_bronze:
        answer = i + 1
        break

print(answer)