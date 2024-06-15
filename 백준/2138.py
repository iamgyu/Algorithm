import copy

N = int(input()) # N: 스위치, 전구 갯수

before = list(map(int, input().rstrip()))
after = list(map(int, input().rstrip()))
result = 1e9

# 1번 전구 안누르는 경우
count = 0 # 스위치 누르는 횟수
status = copy.deepcopy(before) # 초기값 깊은 복사

for i in range(1, N):
    if status[i - 1] != after[i - 1]:
        count += 1
        if status[i] == 0:
            status[i] = 1
        else:
            status[i] = 0

        if i < N - 1:
            if status[i + 1] == 0:
                status[i + 1] = 1
            else:
                status[i + 1] = 0

if status[N - 1] == after[N - 1]:
    result = count

# 1번 전구를 누르는 경우
count = 1 # 스위치 누르는 횟수
status = copy.deepcopy(before)
if status[0] == 0:
    status[0] = 1
else:
    status[0] = 0

if status[1] == 0:
    status[1] = 1
else:
    status[1] = 0

for i in range(1, N):
    if status[i - 1] != after[i - 1]:
        count += 1
        if status[i] == 0:
            status[i] = 1
        else:
            status[i] = 0

        if i < N - 1:
            if status[i + 1] == 0:
                status[i + 1] = 1
            else:
                status[i + 1] = 0

if status[N - 1] == after[N - 1]:
    result = min(result, count)

print(-1 if result == 1e9 else result)