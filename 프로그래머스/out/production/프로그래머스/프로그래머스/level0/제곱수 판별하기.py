def solution(n):
    for i in range(1, 1001):
        if n == i * i:
            return 1
    return 2