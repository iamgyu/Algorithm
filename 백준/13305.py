N = int(input()) # 도시의 개수
road_length = list(map(int, input().split())) # 도로의 길이 왼쪽부터 N-1개
oil_price = list(map(int, input().split())) # 리터당 오일 가격 왼쪽부터 N개

min_cost = 0 # 최소 비용
min_oil_price = oil_price[0] # 최소 오일 가격

for i in range(N - 1):
    if min_oil_price > oil_price[i]:
        min_oil_price = oil_price[i]

    min_cost += min_oil_price * road_length[i]

print(min_cost)