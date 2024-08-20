from itertools import combinations
n = int(input())
member = [i for i in range(1, n + 1)]
arr = [list(map(int, input().split())) for _ in range(n)]

ans = 1e9
for team1 in list(combinations(member, n // 2)):
    team2 = list(set(member) - set(team1))
    score1 = 0
    score2 = 0

    for i in range(n // 2):
        for j in range(i, n // 2):
            if i != j:
                score1 += arr[team1[i] - 1][team1[j] - 1]
                score1 += arr[team1[j] - 1][team1[i] - 1]
                score2 += arr[team2[i] - 1][team2[j] - 1]
                score2 += arr[team2[j] - 1][team2[i] - 1]
    ans = min(ans, abs(score1 - score2))
print(ans)