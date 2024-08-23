import sys
n = int(sys.stdin.readline())
s = sys.stdin.readline().rstrip()
num_arr = [int(sys.stdin.readline()) for _ in range(n)]
stack = []

for i in range(len(s)):
    if 'A' <= s[i] <= 'Z':
        stack.append(num_arr[ord(s[i]) - ord('A')])
    else:
        num2 = stack.pop()
        num1 = stack.pop()

        if s[i] == '+':
            stack.append(num1 + num2)
        elif s[i] == '-':
            stack.append(num1 - num2)
        elif s[i] == '*':
            stack.append(num1 * num2)
        elif s[i] == '/':
            stack.append(num1 / num2)

print('%.2f' % stack[0])