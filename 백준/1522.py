str = input()
count_a = str.count('a')

answer = 1000
for i in range(len(str)):
    temp = []
    num = 0

    while num < count_a:
        temp.append(str[(i + num) % len(str)])
        num += 1

    if answer > temp.count('b'):
        answer = temp.count('b')

print(answer)