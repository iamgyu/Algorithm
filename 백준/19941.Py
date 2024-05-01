N, K = map(int, input().split()) # N: 사람 수, K: 햄버거를 선택할 수 있는 거리
str = input() # P는 사람, H는 햄버거

check = [0] * 20000 # 이미 먹은 햄버거인지 체크를 위한 배열
maxPeople = 0 # 햄버거를 먹을 수 있는 사람의 최대 수

for i in range(N):
    next = False
    if K > i:
        if str[i] == 'P':
            temp = 0
            while temp < i:
                if str[temp] == 'H' and check[temp] == 0:
                    check[temp] = 1
                    maxPeople += 1
                    next = True
                    break;
                else:
                    temp += 1
            
            if not next:
                for j in range(i + 1, i + K + 1):
                    if j < N:
                        if str[j] == 'H' and check[j] == 0:
                            check[j] = 1
                            maxPeople += 1
                            break;

    elif K + i > N - 1:
        if str[i] == 'P':
            for j in range(i - K , i):
                if str[j] == 'H' and check[j] == 0:
                    check[j] = 1
                    maxPeople += 1
                    next = True
                    break;

            if not next:
                temp = i + 1
                while temp < len(str):
                    if str[temp] == 'H' and check[temp] == 0:
                        check[temp] = 1
                        maxPeople += 1
                        break;
                    else:
                        temp += 1

    else:
        next = False
        if str[i] == 'P':
            for j in range(i - K , i):
                if str[j] == 'H' and check[j] == 0:
                    check[j] = 1
                    maxPeople += 1
                    next = True
                    break;
            
            if not next:
                for j in range(i + 1, i + K + 1):
                    if str[j] == 'H' and check[j] == 0:
                        check[j] = 1
                        maxPeople += 1
                        break;

print(maxPeople)