N, score, P = map(int, input().split())

count = 0
rank = 1

try:
    scores = list(map(int, input().split()))
except EOFError:
    scores = []

for i in range(N):
    if scores[i] >= score:
        count += 1
    if scores[i] > score:
        rank += 1

if count >= P:
    print(-1)
else:
    print(rank)