def func(n, number, string):
    if number == n:
        result = eval(string.replace(' ', ''))
        if result == 0:
            answer.append(string)
        return
    
    else:
        func(n, number + 1, string + ' ' + str(number + 1))
        func(n, number + 1, string + '+' + str(number + 1))
        func(n, number + 1, string + '-' + str(number + 1))

N = int(input()) # N: 테스트 케이스 수

for i in range(N):
    num = int(input()) # 입력 수
    answer = []

    func(num, 1, '1')
    for s in answer:
        print(s)

    print()