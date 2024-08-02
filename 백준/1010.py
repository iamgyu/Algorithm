T = int(input())

def factorial(n):
    return n * factorial(n - 1) if n > 1 else 1

for i in range(T):
    n, m = map(int, input().split()) # n: 서쪽 사이트, m: 동쪽 사이트

    result = factorial(m) // (factorial(m - n) * factorial(n))

    print(result)