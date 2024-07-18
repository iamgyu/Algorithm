from collections import deque

T = int(input())

for i in range(T):
    N, M = map(int, input().split()) # N : 문서의 개수, M : 몇 번째 놓여있는지 위치

    queue = deque(list(map(int, input().split())))
    count = 0
    