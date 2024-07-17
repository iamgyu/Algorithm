N = int(input())
arr = [] # 입력을 받기 위한 배열
stack = [] # 회의를 저장하기 위한 스택
for i in range(N):
    start, end = map(int, input().split())
    arr.append((start, end))

arr.sort(key=lambda x: (x[1], x[0]))
start_time = 0
ans = 0

for i in range(N):
    if arr[i][0] >= start_time:
        start_time = arr[i][1]
        ans += 1

print(ans)