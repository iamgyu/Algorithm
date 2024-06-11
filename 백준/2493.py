N = int(input()) # N: 탑의 수
arr = list(map(int, input().split())) # 탑들의 높이
answer = [0 for _ in range(N)] # 정답 리스트
stack = [] # 스택 리스트

stack.append((arr[-1], N - 1))
for i in range(N - 2, -1, -1):    
    if stack[-1][0] < arr[i]:
        while stack and stack[-1][0] < arr[i]:
            num, loc = stack.pop()
            answer[loc] = i + 1
    stack.append((arr[i], i))

print(' '.join(str(x) for x in answer))