import math
# n: 과일 종류수, m: 훔칠 과일 수
n = int(input())
m = int(input())

# 적어도 각 종류를 하나씩은 훔친다
# 한종류씩 훔치는 걸 빼고 중복조합으로 풀이
m -= n

answer = math.factorial(m + n - 1) // (math.factorial(n - 1) * math.factorial(m))
print(answer)