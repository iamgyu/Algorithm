def solution(score):
    answer = []
    a = [sum(i) / 2 for i in score]
    b = sorted(a, reverse = True)
    for i in a:
        answer.append(b.index(i) + 1)
    return answer