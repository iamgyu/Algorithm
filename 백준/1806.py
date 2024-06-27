N, S = map(int, input().split())
arr = list(map(int, input().split()))

start = 0
end = 0
answer = int(1e9)
total = arr[start]

while start <= end:

    if total < S:
        end += 1
        if end > N - 1:
            if start == 0:
                answer = 0
            break
        else:
            total += arr[end]
    else:
        if answer > end - start + 1:
            answer = end - start + 1
        total -= arr[start]
        start += 1

print(answer)