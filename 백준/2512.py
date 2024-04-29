N, X = int(input()) # 지방의 수
budget = list(map(int, input().split())) # N개의 지방 예산
country_budget = int(input()) # 전체 국가예산
start, end = 0, max(budget) # 시작 끝

while start <= end:
    total = 0 # 지방 예산 합
    mid = (start + end) // 2 # 상한 값

    for i in budget:
        if i > mid:
            total += mid
        else:
            total += i
    
    if total > country_budget:
        end = mid - 1
    else:
        start = mid + 1

print(end)