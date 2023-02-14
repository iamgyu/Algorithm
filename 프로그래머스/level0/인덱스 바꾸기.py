def solution(my_string, num1, num2):
    a = my_string[num1]
    b = my_string[num2]
    answer = list(my_string)
    answer[num1] = b
    answer[num2] = a
    return ''.join(answer)