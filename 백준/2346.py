from collections import deque

N = int(input()) # N: 자연수
arr = list(map(int, input().split())) # arr: 풍선안에 들어가 있는 숫자 모음
q = deque()
ans = []

for i in range(N):
    q.append((i + 1, arr[i]))

while q:
    index, num = q.popleft()
    ans.append(index)

    if not q:
        break

    if num > 0:
        for i in range(num - 1):
            index, num = q.popleft()
            q.append((index, num))
    else:
        for i in range(abs(num)):
            index, num = q.pop()
            q.appendleft((index, num))

print(' '.join(map(str, ans)))