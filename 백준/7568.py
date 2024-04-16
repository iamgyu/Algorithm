n = int(input())

arr = [[0 for col in range(2)] for row in range(n)]

for i in range(n):
    arr[i][0], arr[i][1] = map(int, input().split())
    
for i in arr:
    rank = 1
    for j in arr:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    
    print(rank, end = " ")