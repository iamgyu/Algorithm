a = int(input())

# 1 7 19 37 61
# 0 6 12 18 24
# n(A) = 6(n-1) + (n-2)

hexa = 1
answer = 0
while(a > hexa):
    hexa = 6 * answer + hexa
    answer += 1

if a == 1:
    answer = 1
    
print(answer)