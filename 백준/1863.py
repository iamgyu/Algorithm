N = int(input()) # N: 갯수

stack = []
answer = 0

for i in range(N):
    x, y = map(int, input().split())

    if not stack:
        stack.append(y)
        continue
    
    if stack and stack[-1] > y:
        while stack and stack[-1] > y:
            stack.pop()
            answer += 1
        
        if not stack or stack[-1] < y:
            stack.append(y)
    else:
        stack.append(y)

for i in range(len(stack)):
    num = stack.pop()
    if num != 0:
        answer += 1

print(answer)