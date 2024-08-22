n = int(input()) # n: 파일의 개수
file_arr = [input() for _ in range(n)]
ans = {}

for i in range(n):
    idx = file_arr[i].find('.')
    temp = file_arr[i][idx + 1:]

    if temp not in ans:
        ans[temp] = 1
    else:
        ans[temp] += 1

ans = sorted(ans.items())

for item, value in ans:
    print(item, value)