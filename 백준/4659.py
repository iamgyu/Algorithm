vowel = ['a', 'i', 'o', 'u', 'e']

while True:
    password = input()

    if password == "end":
        break

    if not any(c in password for c in vowel):
        print("<" + password + ">" + " is not acceptable.")
        continue
    
    vowel_count = 0
    consonant_count = 0
    flag = True
    temp = ''

    for c in password:
        if c in vowel:
            vowel_count += 1
            consonant_count = 0
        else:
            consonant_count += 1
            vowel_count = 0

        if vowel_count >= 3 or consonant_count >= 3:
            flag = False

        if temp == c:
            if c == 'e' or c == 'o':
                pass
            else:
                flag = False

        temp = c

    if flag:
        print("<" + password + ">" + " is acceptable.")
    else:
        print("<" + password + ">" + " is not acceptable.")