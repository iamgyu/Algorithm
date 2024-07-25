N, M = map(int, input().split()) # N: 기차의 수, M: 명령의 수
train = [[0 for _ in range(21)] for _ in range(N + 1)]

for i in range(M):
    command = list(map(int, input().split()))
    
    # 명령1. i번째 기차에 x좌석에 사람을 태움. 있는 경우 행동 생략
    if command[0] == 1:
        train[command[1]][command[2]] = 1
    # 명령2. i번째 기차에 x좌석 사람을 하차. 없는 경우 행동 생략
    elif command[0] == 2:
        train[command[1]][command[2]] = 0
    # 명령3. i번째 기차에 앉아 있는 사람들 모두 한칸씩 뒤로 이동. 20번째 자리에 앉은 사람은 명령 후 하차
    elif command[0] == 3:
        if train[command[1]][20] == 1:
            train[command[1]][20] = 0
        for j in range(20, 0, -1):
            if train[command[1]][j - 1] == 1:
                train[command[1]][j] = train[command[1]][j - 1] 
                train[command[1]][j - 1] = 0
    # 명령4. i번째 기차에 앉아 있는 사람들 모두 한칸씩 앞으로 이동. 1번째 자리에 앉은 사람은 명령 후 하차
    elif command[0] == 4:
        if train[command[1]][1] == 1:
            train[command[1]][1] = 0
        for j in range(1, 20):
            if train[command[1]][j + 1] == 1:
                train[command[1]][j] = train[command[1]][j + 1]
                train[command[1]][j + 1] = 0

record = []
ans = 0
for i in range(1, N + 1):
    if train[i] not in record:
        record.append(train[i])
        ans += 1

print(ans)