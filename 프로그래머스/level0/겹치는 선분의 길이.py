def solution(lines):
    answer = 0
    count = [0 for _ in range(200)]
    for l in lines:
        for i in range(l[0], l[1]):
            count[i + 100] += 1
    answer += count.count(2)
    answer += count.count(3)
    return answer