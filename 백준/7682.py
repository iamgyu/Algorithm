check = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

while True:
    answer = False
    str = input()

    if str == "end":
        break

    x_count = str.count('X')
    o_count = str.count('O')
    dot_count = str.count('.')

    x_win = False
    o_win = False

    for l in check:
        if str[l[0]] == str[l[1]] == str[l[2]] == 'X':
            x_win = True

    for l in check:
        if str[l[0]] == str[l[1]] == str[l[2]] == 'O':
            o_win = True

    if (x_win and not o_win and x_count == o_count + 1)\
       or (not x_win and o_win and x_count == o_count)\
       or (not x_win and not o_win and x_count == 5 and o_count == 4):
        answer = True
    
    if answer:
        print("valid")
    else:
        print("invalid")