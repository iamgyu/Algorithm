str = input()
words = []

for i in range(1, len(str)):
    for j in range(i + 1, len(str)):
        part1 = ''.join(reversed(str[:i]))
        part2 = ''.join(reversed(str[i:j]))
        part3 = ''.join(reversed(str[j:]))

        words.append(part1 + part2 + part3)

print(sorted(words)[0])