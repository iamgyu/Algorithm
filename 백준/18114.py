N, C = map(int, input().split()) # N: 물건 갯수, C: 목표 무게
arr = list(map(int, input().split()))
arr.sort()
ans = 0

# 물건 1개 선택 시 확인
if C in arr:
    ans = 1

# 물건 2개 선택 시 확인
left = 0
right = N - 1
while left < right:
    if arr[left] + arr[right] == C:
        ans = 1
        break
    
    if arr[left] + arr[right] < C:
        left += 1
    else:
        right -= 1

# 물건 3개 선택 시 확인
for i in range(N - 2):
    left = i + 1
    right = N - 1
    while left < right:
        if arr[left] + arr[right] + arr[i] == C:
            ans = 1
            break

        if arr[left] + arr[right] + arr[i] < C:
            left += 1
        else:
            right -= 1

print(ans)