num = input() # 입력 값
N = 0 # 최솟값

while True:
    N += 1
    temp = str(N) # 비교를 위해 문자열로 변환

    while len(temp) > 0 and len(num) > 0:
        if temp[0] == num[0]:
            num = num[1:]
        temp = temp[1:]
    
    if num == '':
        print(N)
        break;