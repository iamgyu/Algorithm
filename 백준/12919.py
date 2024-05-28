S = input() # 첫 번째 문자열
T = input() # 두 번째 문자열

answer = 0

def recursion(word):
    global answer

    if S == word:
        answer = 1
        return
    
    if len(word) == 0:
        return
    
    if word[-1] == 'A':
        recursion(word[:-1])
    
    if word[0] == 'B':
        recursion(word[1:][::-1])

recursion(T)
print(answer)