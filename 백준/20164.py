s = input()

max_v = 0
min_v = 1e9

def check(s):
    count = 0
    for c in s:
        if int(c) % 2 == 1:
            count += 1
    return count

def cut(s, count):
    global max_v, min_v

    if len(s) == 1:
        max_v = max(max_v, count)
        min_v = min(min_v, count)
    
    elif len(s) == 2:
        temp = str(int(s[0]) + int(s[1]))
        cut(temp, count + check(temp))
    
    else:
        for i in range(1, len(s)):
            for j in range(i + 1, len(s)):
                part1 = s[:i]
                part2 = s[i:j]
                part3 = s[j:]
                temp = str(int(part1) + int(part2) + int(part3))
                cut(temp, count + check(temp))

cut(s, check(s))
print(min_v, max_v)