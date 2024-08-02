N = int(input()) # N: 무게

# 3과 5를 조합해서 구하는 과정
ans = 1
temp = N
while temp > 0:
    temp -= 3

    if temp % 5 == 0:
        ans += temp // 5
        break
    
    ans += 1
if temp < 0:
    ans = 1e9

# 3으로만 구하는 경우
ans3 = 1e9
if N % 3 == 0:
    ans3 = N // 3

# 5로만 구하는 경우
ans5 = 1e9
if N % 5 == 0:
    ans5 = N // 5

if ans == 1e9 and ans3 == 1e9 and ans5 == 1e9:
    print(-1)
else:
    print(min(ans, ans3, ans5))