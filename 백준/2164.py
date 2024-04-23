from collections import deque

N = int(input())

dq = deque()

for i in range(N):
    dq.append(i + 1)

while len(dq) != 1:
    dq.popleft()
    first_element = dq.popleft()
    dq.append(first_element)

print(dq[0])