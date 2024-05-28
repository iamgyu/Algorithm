N, K = map(int, input().split())  # N: 길이, K: 내구도가 0인 칸의 개수 상한선
arr = list(map(int, input().split()))  # 2N만큼의 입력 값
belt = []  # (내구도, 로봇유무)로 추가될 예정
answer = 0  # 몇 번째 단계인지 세기
count = 0  # 내구도가 0인 칸 개수

for i in range(len(arr)):
    belt.append([arr[i], False])

def shift_list(l):
    if l:
        last = l.pop()
        l.insert(0, last)
    return l

while count < K:
    # 1. 벨트가 로봇이랑 함께 회전, 회전 후 내리는 위치에 로봇이 있으면 로봇 내림
    belt = shift_list(belt)
    if belt[N - 1][1] == True:
        belt[N - 1][1] = False

    # 2. 가장 먼저 벨트에 올라간 로봇부터 이동가능하면 이동
    for i in range(N - 1, 0, -1):
        if belt[i - 1][1] == True and belt[i][0] > 0 and not belt[i][1]:
            belt[i][0] -= 1
            belt[i][1] = True
            belt[i - 1][1] = False

    # 이동 후, 내리는 위치에 로봇이 있으면 내림
    if belt[N - 1][1] == True:
        belt[N - 1][1] = False

    # 3. 올리는 위치에 있는 칸의 내구도가 0이 아니면 로봇 올림
    if belt[0][0] > 0:
        belt[0][1] = True
        belt[0][0] -= 1

    # 내구도가 0인 칸 개수 세기
    count = sum(1 for b in belt if b[0] == 0)
    answer += 1

print(answer)