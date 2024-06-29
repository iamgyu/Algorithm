N, C = map(int, input().split()) # N: 집 개수, C: 공유기 개수

arr = []

for i in range(N):
    arr.append(int(input()))

arr.sort()

start = 1
end = arr[-1] - arr[0]
answer = 0

while start <= end:
    mid = (start + end) // 2
    current = arr[0]
    count = 1

    for i in range(1, len(arr)):
        if arr[i] >= current + mid:
            current = arr[i]
            count += 1

    if C <= count:
        start = mid + 1
        answer = mid
    else:
        end = mid - 1

print(answer)