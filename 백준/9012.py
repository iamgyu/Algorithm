N = int(input())
ans = []
for i in range(N):
    temp = input()
    stack = []

    for i in range(len(temp)):
        if temp[i] == '(':
            stack.append(temp[i])
        else:
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(temp[i])
    if not stack:
        ans.append("YES")
    else:
        ans.append("NO")

for i in range(len(ans)):
    print(ans[i])