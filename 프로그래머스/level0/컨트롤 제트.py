def solution(s):
    answer = 0
    t = s.split()
    for i in range(len(t)):
        if t[i] != 'Z':
            answer += int(t[i])
        else:
            answer -= int(t[i-1])
    return answer