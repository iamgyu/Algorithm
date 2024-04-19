N = int(input())

board = []

for i in range(N):
    board.append(list(input().strip()))

heart_x, heart_y = 0, 0

for i in range(1, N):
    for j in range(N - 1):
        if board[i][j] == '*' and board[i][j + 1] == '*':
            if board[i - 1][j + 1] == '*':
                heart_x, heart_y = i + 1, j + 2
                break

left_arm, right_arm = 0, 0
waist, waist_x, waist_y = 0, 0, 0
left_leg, right_leg = 0, 0

for i in range(heart_y - 2, -1, -1):
    if board[heart_x - 1][i] == '*':
        left_arm += 1
    else:
        break

for i in range(heart_y, N):
    if board[heart_x - 1][i] == '*':
        right_arm += 1
    else:
        break

for i in range(heart_x, N):
    if board[i][heart_y - 1] == '*':
        waist += 1
    else:
        waist_x, waist_y = i - 1, heart_y - 1
        break

for i in range(waist_x + 1, N):
    if board[i][waist_y - 1] == '*':
        left_leg += 1
    else:
        break

for i in range(waist_x + 1, N):
    if board[i][waist_y + 1] == '*':
        right_leg += 1
    else:
        break

print(heart_x, heart_y)
print(left_arm, right_arm, waist, left_leg, right_leg)