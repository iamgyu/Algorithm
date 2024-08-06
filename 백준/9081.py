t = int(input()) # t: 테스트 개수

for t in range(t):
    s = list(input())
    i, j = 0, 1

    for idx in range(1, len(s)):
        if s[idx - 1] < s[idx] and i < idx:
            i = idx

    for idx in range(1, len(s)):
        if s[i - 1] < s[idx] and j < idx:
            j = idx

    if i != 0 and j != 0:
        s[i - 1], s[j] = s[j], s[i - 1]
        s[i:] = list(reversed(s[i:]))
    
    print(''.join(s))