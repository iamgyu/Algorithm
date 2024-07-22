seed = int(input())
chart = list(map(int, input().split()))

# 1. BNP 결과 계산
bnp_money = seed # BNP 시드머니
bnp_count = 0 # BNP 주식 수
for i in range(len(chart) - 1):
    if bnp_money >= chart[i]:
        bnp_count += bnp_money // chart[i]
        bnp_money = bnp_money % chart[i]

bnp_result = bnp_count * chart[-1] + bnp_money

# 2. TIMING 결과 계산
timing_money = seed # TIMING 시드머니
timing_count = 0 # TIMING 주식 수
up = 0 # 연속 가격 상승 변수
down = 0 # 연속 가격 하락 변수
for i in range(1, len(chart) - 1):
    # 상승과 하락 체크
    if chart[i - 1] < chart[i]:
        up += 1
        down = 0
    elif chart[i - 1] > chart[i]:
        down += 1
        up = 0
    else:
        up = 0
        down = 0
    

    if up >= 3: # 연속 가격 상승이 3일 이상이면
        # 전량 매도
        timing_money += timing_count * chart[i]
        timing_count = 0
    elif down >= 3: # 연속 가격 하락이 3일 이상이면
        if timing_money >= chart[i]: # 시드 머니가 차트 가격보다 높은 경우
            timing_count += timing_money // chart[i] # 전량 매수
            timing_money = timing_money % chart[i]

timing_result = timing_count * chart[-1] + timing_money

if bnp_result > timing_result:
    print("BNP")
elif timing_result > bnp_result:
    print("TIMING")
else:
    print("SAMESAME")