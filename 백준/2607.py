n = int(input())
word = input()

word_list = list(word)
answer = 0

for i in range(n - 1):
    w = input()
    temp = word_list.copy()
    diff = 0

    for c in w:
        if c in temp:
            temp.remove(c)
        else:
            diff += 1

    if diff < 2 and len(temp) < 2:
        answer += 1

print(answer)