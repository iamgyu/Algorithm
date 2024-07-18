N = int(input()) # 입력의 수
stack = []
ans = []
for i in range(N):
    word = input().split()

    if word[0] == 'push':
        stack.append(word[1])

    elif word[0] == 'pop':
        if not stack:
            ans.append(-1)
        else:
            ans.append(stack.pop())

    elif word[0] == 'size':
        ans.append(len(stack))

    elif word[0] == 'empty':
        if not stack:
            ans.append(1)
        else:
            ans.append(0)

    elif word[0] == 'top':
        if not stack:
            ans.append(-1)
        else:
            ans.append(stack[-1])

for i in range(len(ans)):
    print(ans[i])