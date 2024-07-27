board = [] # 바둑판
for i in range(19):
    board.append(list(map(int, input().split())))

# 검은 바둑알은 1, 흰 바둑알은 2, 놓이지 않는 곳은 0
# 8방향 상하좌우 좌상, 좌하, 우상, 우하 대각선 체크

# 5개가 연속으로 같은 바둑 알인지 확인하고 좌표 리턴, 아닌 경우 빈 값 리턴
def checkWin(checkNum, i, j):
    result = []
    # 상 체크
    count = 1 # 같은 숫자가 몇 번이나 연속되는지 확인
    for k in range(1, len(board)):
        if i - k >= 0 and board[i - k][j] == checkNum:
            count += 1
        else:
            break
    if count == 5:
        ok = True
        if i - 5 >= 0 and board[i - 5][j] == checkNum:
            ok = False
        if i + 1 < len(board) and board[i + 1][j] == checkNum:
            ok = False
        if ok:
            result.append((i - 4 + 1, j + 1))
    
    # 하 체크
    count = 1
    for k in range(1, len(board)):
        if i + k < len(board) and board[i + k][j] == checkNum:
            count += 1
        else:
            break
    if count == 5:
        ok = True
        if i - 1 >= 0 and board[i - 1][j] == checkNum:
            ok = False
        if i + 5 < len(board) and board[i + 5][j] == checkNum:
            ok = False
        if ok:
            result.append((i + 1, j + 1))
    
    # 좌 체크
    count = 1
    for k in range(1, len(board)):
        if j - k >= 0 and board[i][j - k] == checkNum:
            count += 1
        else:
            break
    if count == 5:
        ok = True
        if j - 5 >= 0 and board[i][j - 5] == checkNum:
            ok = False
        if j + 1 < len(board) and board[i][j + 1] == checkNum:
            ok = False
        if ok: 
            result.append((i + 1, j - 4 + 1))

    # 우 체크
    count = 1
    for k in range(1, len(board)):
        if j + k < len(board) and board[i][j + k] == checkNum:
            count += 1
        else:
            break
    if count == 5:
        ok = True
        if j + 5 < len(board) and board[i][j + 5] == checkNum:
            ok = False
        if j - 1 >= 0 and board[i][j - 1] == checkNum:
            ok = False
        if ok:   
            result.append((i + 1, j + 1))
    
    # 좌상 체크
    count = 1
    for k in range(1, len(board)):
        if j - k >= 0 and i - k >= 0 and board[i - k][j - k] == checkNum:
            count += 1
        else:
            break
    if count == 5:
        ok = True
        if i - 5 >= 0 and j - 5 >= 0 and board[i - 5][j - 5] == checkNum:
            ok = False
        if i + 1 < len(board) and j + 1 <= len(board) and board[i + 1][j + 1] == checkNum:
            ok = False
        if ok:
            result.append((i - 4 + 1, j - 4 + 1))
    
    # 좌하 체크
    count = 1
    for k in range(1, len(board)):
        if j - k >= 0 and i + k < len(board) and board[i + k][j - k] == checkNum:
            count += 1
        else:
            break
    if count == 5:
        ok = True
        if i + 5 < len(board) and j - 5 >= 0 and board[i + 5][j - 5] == checkNum:
            ok = False
        if i - 1 >= 0 and j + 1 < len(board) and board[i - 1][j + 1] == checkNum:
            ok = False
        if ok:
            result.append((i + 4 + 1, j - 4 + 1))

    # 우상 체크
    count = 1
    for k in range(1, len(board)):
        if j + k < len(board) and i - k >= 0 and board[i - k][j + k] == checkNum:
            count += 1
        else:
            break
    if count == 5:
        ok = True
        if i - 5 >= 0 and j + 5 < len(board) and board[i - 5][j + 5] == checkNum:
            ok = False
        if i + 1 < len(board) and j - 1 >= 0 and board[i + 1][j - 1] == checkNum:
            ok = False
        if ok:
            result.append((i + 1, j + 1))

    # 우하 체크
    count = 1
    for k in range(1, len(board)):
        if j + k < len(board) and i + k < len(board) and board[i + k][j + k] == checkNum:
            count += 1
        else:
            break
    if count == 5:
        ok = True
        if i + 5 < len(board) and j + 5 < len(board) and board[i + 5][j + 5] == checkNum:
            ok = False
        if i - 1 >= 0 and j - 1 >= 0 and board[i - 1][j - 1] == checkNum:
            ok = False
        if ok:
            result.append((i + 1, j + 1))

    return result        

answer = []
for i in range(19):
    for j in range(19):
        if board[i][j] == 1 or board[i][j] == 2:
            checkNum = board[i][j]
            
            # 5개가 연속으로 같은 바둑 알인지 확인
            answer = checkWin(checkNum, i, j)
            if answer:
                print(checkNum)
                print(answer[0][0], answer[0][1])
                break
    if answer:
        break
if not answer:
    print(0)