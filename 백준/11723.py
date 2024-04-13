import sys

M = int(sys.stdin.readline())

s = set()

for i in range(M):
    cal = sys.stdin.readline().split()
    if cal[0] == 'all':
        s = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}
    elif cal[0] == 'empty':
            s = set()
    else:
        n = int(cal[1])
        if cal[0] == 'add':
            if n not in s:
                s.add(n)
        elif cal[0] == 'remove':
            if n in s:
                s.remove(n)
        elif cal[0] == 'check':
            if n in s:
                print(1)
            else:
                print(0)
        elif cal[0] == 'toggle':
            if n in s:
                s.remove(n)
            else:
                s.add(n)