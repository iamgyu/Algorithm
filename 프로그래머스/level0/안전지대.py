def solution(board):
    new_list = [[i, j] for i in range(len(board)) for j in range(len(board[i])) if board[i][j] == 1]
    answer = len(new_list)
    for n in new_list:
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                if 0 <= n[0] + i < len(board) and 0 <= n[1] + j < len(board):
                    if board[n[0] + i][n[1] + j] == 0:
                        board[n[0] + i][n[1] + j] = 1
                        answer += 1
    return len(board) ** 2 - answer