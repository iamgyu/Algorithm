s = list(input())
bomb = input()
stack = []

for i in range(len(s)):
    stack.append(s[i])

    if len(bomb) <= len(stack) and ''.join(stack[-len(bomb):]) == bomb:
        for j in range(len(bomb)):
            stack.pop()

if len(stack) == 0:
    print("FRULA")
else:
    print(''.join(stack))