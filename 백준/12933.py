str = input()

ans = 0 # 정답을 위한 변수
count = 0 # 현재 temp에 오리가 몇 마리가 있는지 알기 위함
temp = [] # 'q', 'u', 'a', 'c', 'k' 순으로 들어가야함

for i in range(len(str)):
    if i == 0 and str[i] != 'q':
        ans = -1
        break

    if str[i] == 'q':
        temp.append([str[i]])
    else:
        found = False
        for j in range(len(temp)):
            if str[i] == 'u' and temp[j][-1] == 'q':
                    temp[j].append(str[i])
                    found = True
                    break
            elif str[i] == 'a' and temp[j][-1] == 'u':
                    temp[j].append(str[i])
                    found = True
                    break
            elif str[i] == 'c' and temp[j][-1] == 'a':
                    temp[j].append(str[i])
                    found = True
                    break
            elif str[i] == 'k' and temp[j][-1] == 'c':
                    temp[j].append(str[i])
                    # *이 조건이 중요*
                    if len(temp[j]) == 5:
                         temp.pop(j)
                    found = True
                    break

        if not found:
            ans = -1
            break

    count = len(temp)
    ans = max(ans, count)

if len(temp) != 0:
    ans = -1
    
print(ans)