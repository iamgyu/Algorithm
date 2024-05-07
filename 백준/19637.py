N, M = map(int, input().split()) # N: 칭호 개수, M: 캐릭터들 개수

name_arr = ['' for i in range(N)] # 칭호 배열
score_arr = [0 for i in range(N)] # 기준 점수 배열
char_arr = ['' for i in range(M)] # 캐릭터 칭호 

for i in range(N):
    name, score = input().split()

    name_arr[i] = name
    score_arr[i] = int(score)

for i in range(M):
    s = int(input())

    start, end = 0, N - 1

    while start <= end:
        mid = (start + end) // 2

        if score_arr[mid] >= s:
            end = mid - 1
        else:
            start = mid + 1
    
    char_arr[i] = name_arr[start]


for i in range(M):
    print(char_arr[i])