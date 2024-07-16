N = int(input())
arr = list(map(int, input().split()))
arr.sort()

min = 1e9
ans = 0

for i in range(arr[0], arr[-1] + 1):
    temp = 0
    for j in range(N):
        temp += abs(arr[j] - i)
    if temp < min:
        min = temp
        ans = i
    
print(ans)