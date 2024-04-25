N = int(input()) # 굴다리의 길이
M = int(input()) # 가로등의 개수
x = list(map(int, input().split())) # 가로등의 위치

h = 0 # 가로등의 높이

if M == 1:
    h = x[0] if x[0] > N - x[0] else N - x[0]
else:
    h = x[0] # 0에서 처음 가로등까지 거리, 즉 가로등의 최소 높이
    for i in range(len(x) - 1):
        center_h = 0
        center_distance = x[i + 1] - x[i]

        if center_distance % 2 == 1:
            center_h = center_distance // 2 + 1
        else:
            center_h = center_distance // 2
        
        if h < center_h:
            h = center_h
    
    if h < N - x[-1]:
        h = N - x[-1]
        

print(h)