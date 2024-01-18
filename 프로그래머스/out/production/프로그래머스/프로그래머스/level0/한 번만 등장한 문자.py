def solution(s):
    answer = ''
    arr = [0 for i in range(26)]
    for i in s:
        arr[ord(i) - 97] += 1
        
    for i in range(26):
        if arr[i] == 1:
            answer += chr(i + 97)
    return answer