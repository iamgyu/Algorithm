N = int(input()) # 볼의 개수
input_list = list(input()) # 볼 색깔 문자열
red_list_front = input_list.copy()
red_list_front.reverse()
red_list_last = input_list.copy()
blue_list_front = input_list.copy()
blue_list_front.reverse()
blue_list_last = input_list.copy()

# 1. 빨강 옮기는 경우
count_red_last = 0
last = red_list_last.pop()

while red_list_last:
    value = red_list_last.pop()

    if last == 'B' and value == 'R':
        count_red_last += 1
    else:
        last = value

count_red_front = 0
last = red_list_front.pop()

while red_list_front:
    value = red_list_front.pop()

    if last == 'B' and value == 'R':
        count_red_front += 1
    else:
        last = value

count_red = count_red_last if count_red_last < count_red_front else count_red_front

# 2. 파랑을 옮기는 경우
count_blue_last = 0
last = blue_list_last.pop()

while blue_list_last:
    value = blue_list_last.pop()

    if last == 'R' and value == 'B':
        count_blue_last += 1
    else:
        last = value

count_blue_front = 0
last = blue_list_front.pop()

while blue_list_front:
    value = blue_list_front.pop()

    if last == 'R' and value == 'B':
        count_blue_front += 1
    else:
        last = value

count_blue = count_blue_last if count_blue_last < count_blue_front else count_blue_front

print(count_red if count_red < count_blue else count_blue)