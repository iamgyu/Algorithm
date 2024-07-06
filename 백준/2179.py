N = int(input())
arr = [input() for _ in range(N)]
for a in enumerate(arr):
    arr[a[0]] = a

def check(a, b):
    count = 0
    for i in range(min(len(a), len(b))):
        if a[i] == b[i]:
            count += 1
        else:
            break
    return count

maxlen = [-1, -1, 0]

for i in range(N):
    for j in range(i + 1, N):
        temp = check(arr[i][1], arr[j][1])
        if temp > maxlen[2]:
            maxlen[0] = i
            maxlen[1] = j
            maxlen[2] = temp
    
print(arr[maxlen[0]][1])
print(arr[maxlen[1]][1])