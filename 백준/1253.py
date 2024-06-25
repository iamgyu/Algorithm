N = int(input()) # N: 입력받을 수
arr = list(map(int, input().split()))
arr.sort()
answer = 0

for i in range(N):
    start = 0
    end = N - 1
    while True:
        if start == i:
            start += 1
        if end == i:
            end -= 1
        
        if start >= end:
            break

        if arr[i] == arr[start] + arr[end]:
            answer += 1
            break
        else:
            if arr[i] < arr[start] + arr[end]:
                end -= 1
            else:
                start += 1

print(answer)