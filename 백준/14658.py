N, M, L, K = map(int, input().split()) # N: 구역 가로, M: 구역 세로, L: 트램펄린 한 변 길이, k: 별똥별 수
stars = []
ans = K + 1

for i in range(K):
    x, y = map(int, input().split())
    stars.append((x, y))

for i in range(K):
    for j in range(K):
        count = 0
        for k in range(K):
            if stars[i][0] <= stars[k][0] <= stars[i][0] + L and stars[j][1] <= stars[k][1] <= stars[j][1] + L:
                count += 1

        if ans > K - count:
            ans = K - count

print(ans)