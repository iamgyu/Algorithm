s_input = input() # 입력으로 사용할 문자
password = input() # 암호

arr = [0] * 200
result = 0

for i in range(len(s_input)):
    index = ord(s_input[i]) - ord('!')
    if arr[index] == 0:
        arr[index] = i + 1

for i in range(len(password)):
    index = ord(password[i]) - ord('!')

    result *= len(s_input)
    result += arr[index]
    result %= 900528

print(result)