N = int(input()) # 빌딩의 개수
arr = list(map(int, input().split()))

def inclination(dx, dy):
    return dy / dx

example = []
ans = 0
for i in range(N):
    count = 0
    left_inclination = 10e9
    right_inclination = -10e9

    for j in range(i - 1, -1, -1):
        temp = inclination(i - j, arr[i] - arr[j])
        if temp < left_inclination:
            count += 1
            left_inclination = temp

    for j in range(i + 1, N):
        temp = inclination(i - j, arr[i] - arr[j])
        if temp > right_inclination:
            count += 1
            right_inclination = temp
    
    example.append(count)
    if count > ans:
        ans = count

print(ans)