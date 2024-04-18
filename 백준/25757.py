N, game = input().split()

player = set()

for i in range(int(N)):
    name = input()

    if name not in player:
        player.add(name)

if game == 'Y':
    print(len(player))
elif game == 'F':
    print(len(player) // 2)
else:
    print(len(player) // 3)