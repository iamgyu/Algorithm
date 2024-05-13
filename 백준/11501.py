T = int(input()) # 테스트 케이스 개수
answer_list = []

for i in range(T):
    N = int(input()) # 날의 수
    stock = list(map(int, input().split())) # 일별 주식 가격
    answer = 0 # 이익 정수

    stock.reverse()
    max_num = stock[0]

    for j in range(1, N):
        if stock[j] < max_num:
            answer += max_num - stock[j]
        else:
            max_num = stock[j]

    answer_list.append(answer)

for i in answer_list:
    print(i)