n = int(input())

for i in range(n):
    num_input = list(map(int, input().split()))
    answer = 0

    for j in range(1, len(num_input) - 1):
        for k in range(j + 1, len(num_input)):
            if num_input[j] > num_input[k]:
                num_input[j], num_input[k] = num_input[k], num_input[j]
                answer += 1


    print(num_input[0], answer)