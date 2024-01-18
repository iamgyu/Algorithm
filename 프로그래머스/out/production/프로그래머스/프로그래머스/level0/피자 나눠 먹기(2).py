def solution(n):
    return min(i for i in range(1, 100) if (i * 6) % n == 0)