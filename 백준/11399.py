N = int(input())
arr = list(map(int, input().split()))
arr.sort()

ans = 0
temp = 0
for i in range(1, N + 1):
    temp += arr[i - 1]
    ans += temp

print(ans)