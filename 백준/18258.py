from collections import deque
import sys
n = int(sys.stdin.readline())
q = deque()

for i in range(n):
    temp = list(sys.stdin.readline().split())

    if temp[0] == "push":
        q.append(temp[1])

    elif temp[0] == "pop":
        if not q:
            print(-1)
        else:
            print(q.popleft())

    elif temp[0] == "size":
        print(len(q))

    elif temp[0] == "empty":
        if not q:
            print(1)
        else:
            print(0)
    
    elif temp[0] == "front":
        if not q:
            print(-1)
        else:
            print(q[0])
    
    elif temp[0] == "back":
        if not q:
            print(-1)
        else:
            print(q[-1])