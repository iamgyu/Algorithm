height, width = map(int, input().split())
arr = list(map(int, input().split()))
answer = 0

for i in range(1, width - 1):
    left = max(arr[:i])
    right = max(arr[i:])

    if min(left, right) > arr[i]:
        answer += min(left, right) - arr[i]

print(answer)