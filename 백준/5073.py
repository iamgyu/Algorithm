while(True):
    number = list(map(int, input().split()))
    number.sort()

    if number[0] == number[1] == number[2] == 0:
        break
    
    if number[0] + number[1] <= number[2]:
        print('Invalid')
    elif number[0] == number[1] == number[2]:
        print('Equilateral')
    elif (number[0] == number[1] and number[1] != number[2]) or (number[1] == number[2] and number[0] != number[1]):
        print('Isosceles')
    else:
        print('Scalene')