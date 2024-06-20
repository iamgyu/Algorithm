N, K, P, X = map(int, input().split()) # N: 층, K: 자릿수, P: 최대 반전 갯수, X: 멈춰서 반전시킬 층

number = [
[1, 1, 1, 0, 1, 1, 1],
[0, 0, 1, 0, 0, 1, 0],
[1, 0, 1, 1, 1, 0, 1],
[1, 0, 1, 1, 0, 1, 1],
[0, 1, 1, 1, 0, 1, 0],
[1, 1, 0, 1, 0, 1, 1],
[1, 1, 0, 1, 1, 1, 1],
[1, 0, 1, 0, 0, 1, 0],
[1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 0, 1, 1]]

X = str(X).zfill(K)
x_transfrom = [number[int(i)] for i in X]

answer = 0

for i in range(1, N + 1):
    num = str(i).zfill(K)
    num_transform = [number[int(n)] for n in num]

    count = 0 
    for a, b in zip(x_transfrom, num_transform):
        for num1, num2 in zip(a, b):
            if num1 != num2:
                count += 1
        if count > P:
            break

    if count <= P and count > 0:
        answer += 1

print(answer)