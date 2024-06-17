N = int(input())
arr = [[] for _ in range(N + 1)]
result = set()

for i in range(1, N + 1):
    arr[int(input())].append(i)

for i in range(1, N + 1):
    visited = [0] * (N + 1)
    stack = []
    stack.append(i)
    visited[i] = 1

    while stack:
        num = stack.pop()

        for j in arr[num]:
            if visited[j] != 1:
                stack.append(j)
                visited[j] = 1
            elif visited[j] and j == i:
                result.add(j)

result = list(result)
result.sort()

print(len(result))
for i in range(len(result)):
    print(result[i])