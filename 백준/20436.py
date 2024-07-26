sl, sr = input().split() # 왼손, 오른손 시작 위치 알파벳
str = input() # 입력해야 할 문자열

leftKey = [['q', 'w', 'e', 'r', 't'], ['a', 's', 'd', 'f', 'g'], ['z', 'x', 'c', 'v', '-']]
rightKey = [['-', 'y', 'u', 'i', 'o' , 'p'], ['-', 'h', 'j', 'k', 'l', '-'], ['b', 'n' ,'m', '-', '-', '-']]

ans = 0

for i in range(len(str)):
    if any(str[i] in l for l in leftKey):
        start_x, start_y = 0, 0
        char_x, char_y = 0, 0
        for j in range(len(leftKey)):
            for k in range(len(leftKey[0])):
                if leftKey[j][k] == sl:
                    start_x, start_y = j, k
                
                if leftKey[j][k] == str[i]:
                    char_x, char_y = j, k

        ans += abs(start_x - char_x) + abs(start_y - char_y) + 1 # 누를 때도 1이 소요되므로 +1
        sl = str[i]
    
    else:
        start_x, start_y = 0, 0
        char_x, char_y = 0, 0
        for j in range(len(rightKey)):
            for k in range(len(rightKey[0])):
                if rightKey[j][k] == sr:
                    start_x, start_y = j, k
                
                if rightKey[j][k] == str[i]:
                    char_x, char_y = j, k
        ans += abs(start_x - char_x) + abs(start_y - char_y) + 1 # 누를 때도 1이 소요되므로 +1
        sr = str[i]

print(ans)