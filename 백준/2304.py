N = int(input()) # 기둥의 개수
arr = [] # 위치, 높이를 저장하기 위한 리스트

for i in range(N):
    L, H = map(int, input().split()) # L: 위치, H: 높이
    arr.append([L, H])

arr.sort(key=lambda x: x[0]) # 위치를 기준으로 정렬
maxHeight = max([loc[1] for loc in arr]) # 최고 높이
maxLocation = 0 # 최고 높이의 위치 
answer = 0 # 정답

maxLoc = arr[0][0] # 최고 높이를 만날때까지 위치 기록
maxH = arr[0][1] # 최고 높이를 만날때까지 높이 기록

for loc, height in arr:
    if height == maxHeight:
        answer += maxH * (loc - maxLoc)
        maxLocation = loc
        break
    if height > maxH:
        answer += maxH * (loc - maxLoc)
        maxH = height
        maxLoc = loc

arr.reverse() # 거꾸로 정렬
maxHeightR = max([loc[1] for loc in arr]) # 최고 높이 거꾸로 정렬 시
maxLocationR = 0 # 최고 높이의 위치 거꾸로 정렬 시

maxLoc = arr[0][0] # 최고 높이를 만날때까지 위치 기록
maxH = arr[0][1] # 최고 높이를 만날때까지 높이 기록

for loc, height in arr:
    if height == maxHeight:
        answer += maxH * (maxLoc - loc)
        maxLocationR = loc
        break
    if height > maxH:
        answer += maxH * (maxLoc - loc)
        maxH = height
        maxLoc = loc


if maxLocation == maxLocationR: # 최고 높이가 하나만 있을 때
    answer += maxHeight
else: # 최고 높이가 하나가 아닐 때
    answer += maxHeight * (maxLocationR - maxLocation + 1)

print(answer)