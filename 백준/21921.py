N, X = map(int, input().split()) # N: 시작하고 지난 일 수, X: X일 동안 최대 방문자
visitant = list(map(int, input().split())) # N일 동안 방문자 수 

sum = 0 # X일 방문자 계산

for i in range(X):
    sum += visitant[i]

maxVisitant = sum  # 최대 방문자 수
maxPeriod = 0 # 최대 방문자 기간

if maxVisitant != 0:
    maxPeriod = 1

for i in range(X, N):
    sum += visitant[i] - visitant[i - X]

    if sum > maxVisitant:
        maxVisitant = sum
        maxPeriod = 1
    elif sum == maxVisitant and maxVisitant != 0:
        maxPeriod += 1

if maxPeriod == 0:
    print("SAD")
else:
    print(maxVisitant)
    print(maxPeriod)