s = list(input())

zero = s.count('0') // 2
one = s.count('1') // 2

s = s[::-1]
for i in range(zero):
    s.remove('0')

s = s[::-1]
for i in range(one):
    s.remove('1')

print(''.join(s))