N, d, k, c = map(int, input().split()) # N: 접시 수, d: 초밥 가짓 수, k: 연속으로 먹는 수, c: 쿠폰 번호
sushi_belt = [] # 벨트 위에 있는 초밥들 리스트
left = 0 # 시작 변수
answer = 0 # 답

for i in range(N):
    sushi = int(input())
    sushi_belt.append(sushi)

while left < N:
    temp = set() # 겹치는 것을 제외하기 위해 set사용
    length = 0 # 행사를 통해 남은 초밥의 갯수를 세기 위함
    count = 0 # 아래 while문을 연속으로 먹는 수 만큼 세기 위한 변수
    num = left # 벨트 위에 초밥을 가져오기 위한 변수

    while count < k:
        temp.add(sushi_belt[num % N])
        num += 1
        count += 1

    if c in temp:
        length = len(temp)
    else:
        length = len(temp) + 1

    if answer < length:
        answer = length
    
    left += 1

print(answer)