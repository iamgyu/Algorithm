n, k = map(int, input().split()) # n: 카드 갯수, k: 셔플 횟수
s_arr = list(map(int, input().split())) # k번 셔플 하고 난 뒤 결과
d_arr = list(map(int, input().split())) # 셔플 방법

def restoration(s_arr, d_arr):
    temp = [0 for _ in range(n)]

    for i in range(n):
        temp[d_arr[i] - 1] = s_arr[i]

    return temp

for i in range(k):
    s_arr = restoration(s_arr, d_arr)

print(*s_arr)