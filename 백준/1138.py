N = int(input()) # 사람 수
arr = [0 for i in range(N)] # 사람 배열
temp = list(map(int, input().split())) # 입력
count = 1

for num in temp:
    small_count = 0 # 나보다 작은 왼쪽에 있는 사람 수
    empty_count = 0 # 빈 공간 체크
    number = num

    if count == 1:
        arr[number] = count
        count += 1

    else:
        for i in range(N):
            if empty_count == num:
                break
            if arr[i] != 0:
                small_count += 1
            else:
                empty_count += 1
                
        if arr[number + small_count] == 0:
            arr[number + small_count] = count
            count += 1
        else:
            while arr[number + small_count] != 0:
                number += 1
            arr[number + small_count] = count
            count += 1

print(*arr)