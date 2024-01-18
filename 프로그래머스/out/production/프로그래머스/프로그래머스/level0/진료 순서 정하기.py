def solution(emergency):
    answer = []
    st = sorted(emergency, reverse = True)
    for i in emergency:
        for j in range(len(emergency)):
            if i == st[j]:
                answer.append(j+1)
        
    return answer