s = input()
stack = []
ans = []

for c in s:
    if not stack and c == '<':
        stack.append(c)
        ans.append(c)
        continue
    elif not stack and c != '<':
        stack.append(c)
        continue

    if stack and stack[-1] == '<':
        if c == '>':
            stack.pop()
            ans.append(c)
        else:
            ans.append(c)
    
    elif stack and stack[-1] != '<':
        if c == '<':
            while stack:
                ans.append(stack.pop())
            stack.append(c)
            ans.append(c)
        elif c == ' ':
            while stack:
                ans.append(stack.pop())
            ans.append(c)
        else:
            stack.append(c)

while stack:
    ans.append(stack.pop())

print(''.join(ans))