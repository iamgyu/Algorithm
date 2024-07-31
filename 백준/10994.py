import sys
n = int(sys.stdin.readline())
arr = [[' ' for _ in range(n * 4 - 3)] for _ in range(n * 4 - 3)]

def fill_star(n, x, y):
    if n == 1:
        arr[x][y] = '*'
        return

    length = n * 4 - 3
    for i in range(length):
        arr[x][y + i] = '*'
        arr[x + i][y] = '*'
        arr[x + length - 1][y + i] = '*'
        arr[x + i][y + length - 1] = '*'
    
    fill_star(n - 1, x + 2, y + 2)

fill_star(n, 0, 0)
for s in arr:
    print(''.join(s))