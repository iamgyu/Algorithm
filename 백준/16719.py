def showActivateStr(str, isActivate):
    result = ""
    for i in range(len(isActivate)):
        if isActivate[i]:
            result += str[i]
    return result

str = input()
isActivate = [False] * len(str)

for i in range(len(str)):
    temp = [] # [(문자열, 활성화 시킨 인덱스)]

    for j in range(len(isActivate)):
        if isActivate[j] == False:
            isActivate[j] = True
            temp.append((showActivateStr(str, isActivate), j))
            isActivate[j] = False
    
    temp.sort()
    print(temp[0][0])
    isActivate[temp[0][1]] = True