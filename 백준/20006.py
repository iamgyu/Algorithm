p, m = map(int, input().split()) # p: 플레이어 수, m: 방의 정원

room = []

for i in range(p):
    flag = False
    l, n = input().split() # l: 레벨, n: 닉네임
    level = int(l)

    for j in range(len(room)):
        if level >= room[j][0] - 10 and level <= room[j][0] + 10 and len(room[j]) != m + 1:
            flag = True
            room[j].append([level, n])
            break

    if not flag:
        room.append([level, [level, n]])

for i in range(len(room)):
    if len(room[i]) == m + 1:
        print("Started!")
    else:
        print("Waiting!")
    
    sort_room = room[i][1:]
    sort_room.sort(key=lambda x: x[1])
    for level, name in sort_room:
        print(level, name)