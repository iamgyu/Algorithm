def solution(quiz):
    answer = []
    for i in quiz:
        if eval(i[:i.find("=")]) == int(i[i.find("=") + 1:]):
            answer.append("O")
        else:
            answer.append("X")
    return answer