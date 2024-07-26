player = []
announcer = []
check = [[False for _ in range(5)] for _ in range(5)]

def checkNum(num):
    for i in range(5):
        for j in range(5):
            if player[i][j] == num:
                check[i][j] = True

def checkBingo():
    count = 0
    # 가로 체크
    for i in range(5):
        if False in check[i]:
            continue
        else:
            count += 1
    
    # 세로 체크
    temp = 0
    while temp < 5:
        for i in range(5):
            if check[i][temp] == False:
                break
            
            if i == 4:
                count += 1
        temp += 1
    
    # 대각선 체크
    for i in range(5):
        if check[i][i] == False:
            break
        if i == 4:
            count += 1
    
    for i in range(5):
        if check[i][5 - i - 1] == False:
            break
        if i == 4:
            count += 1

    return count

for i in range(5):
    player.append(list(map(int, input().split())))

for i in range(5):
    announcer.append(list(map(int, input().split())))

ans = 0
for i in range(5):
    for j in range(5):
        checkNum(announcer[i][j])
        ans += 1

        if checkBingo() >= 3:
            break
        
    if checkBingo() >= 3:
        print(ans)
        break