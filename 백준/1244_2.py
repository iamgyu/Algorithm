import sys
n = int(sys.stdin.readline()) # n: 스위치 수
switch = list(map(int, sys.stdin.readline().split())) # 스위치 상태 리스트
student_num = int(sys.stdin.readline()) # 학생 수

for i in range(student_num):
    gender, switch_num = map(int, sys.stdin.readline().split())

    if gender == 1: # 남학생인 경우
        plus_num = switch_num
        while switch_num <= n:
            if switch[switch_num - 1] == 1:
                switch[switch_num - 1] = 0
            else:
                switch[switch_num - 1] = 1
            
            switch_num += plus_num
    else: # 여학생인 경우
        side_num = 1
        
        if switch[switch_num - 1] == 1:
            switch[switch_num - 1] = 0
        else:
            switch[switch_num - 1] = 1

        while switch_num - side_num > 0 and switch_num + side_num <= n:
            if switch[switch_num - side_num - 1] == switch[switch_num + side_num - 1] == 1:
                switch[switch_num - side_num - 1] = switch[switch_num + side_num - 1] = 0
            elif switch[switch_num - side_num - 1] == switch[switch_num + side_num - 1] == 0:
                switch[switch_num - side_num - 1] = switch[switch_num + side_num - 1] = 1
            else:
                break

            side_num += 1

for i in range(n):
    if i != 0 and i % 20 == 0:
        print()
    print(switch[i], end=' ')
