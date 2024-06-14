N = int(input()) # N: 용액의 수
arr = list(map(int, input().split())) # 용액의 특성값

start = 0
end = N - 1

answer = []
min = float('inf')

while start < end:
    if abs(arr[start] + arr[end]) < min:
        min = abs(arr[start] + arr[end])
        answer.clear()
        answer.append(arr[start])
        answer.append(arr[end])

    if arr[start] + arr[end] < 0:
        start += 1
    else:
        end -= 1

print(answer[0], answer[1])