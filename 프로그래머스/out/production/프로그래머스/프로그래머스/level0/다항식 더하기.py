def solution(polynomial):
    a, b = 0, 0
    s = polynomial.split(' + ')
    for i in s:
        if i.isdigit():
            b += int(i)
        else:
            a = a + 1 if i == 'x' else a + int(i[:-1])
    
    if a == 0:
        return '{}'.format(b)
    elif a == 1:
        return 'x + {}'.format(b) if b != 0 else 'x'
    else:
        return '{}x + {}'.format(a, b) if b != 0 else '{}x'.format(a)