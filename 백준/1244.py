n = int(input())
light = list(map(int, input().split()))
student_num = int(input())

# 남학생은 1, 여학생은 2
# 출력은 20개씩, 넘어가면 다음 줄에 출력

for i in range(student_num):
    gender, switch_num = map(int, input().split())

    if gender == 1:
        for i in range(switch_num - 1, n, switch_num):
            if light[i] == 1:
                light[i] = 0
            else:
                light[i] = 1
    else:
        if switch_num != 1 and switch_num != n:
            left, right = switch_num - 2, switch_num
            if light[left] == light[right]:
                while light[left] == light[right]:
                    left -= 1
                    right += 1
                    if left < 0 or right >= n:
                        break

                for i in range(left + 1, right):
                    if light[i] == 1:
                        light[i] = 0
                    else:
                        light[i] = 1
            else:
                if light[switch_num - 1] == 1:
                    light[switch_num - 1] = 0
                else:
                    light[switch_num - 1] = 1
        else:                
            if light[switch_num - 1] == 1:
                light[switch_num - 1] = 0
            else:
                light[switch_num - 1] = 1

for i in range(n):
    print(light[i], end=' ')
    if (i + 1) % 20 == 0:
        print()