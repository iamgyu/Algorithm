N = int(input()) # 수열의 길이
arr = list(map(int, input().split())) # 수열
answer = 0
left = 0
right = 0
visited = [False] * 100001

while left < N and right < N:
    if not visited[arr[right]]:
        visited[arr[right]] = True
        right += 1
        answer += right - left
    else:
        visited[arr[left]] = False
        left += 1

print(answer)