input = input()
input = input.upper()
list = [0 for i in range(26)]

for c in input:
    list[ord(c) - 65] += 1

answer = []

for i in range(len(list)):
    if list[i] == max(list):
        answer.append(i)

if len(answer) > 1:
    print('?')
else:
    print(chr(answer[0] + 65))