def solution(num, total):
    answer = [0 for i in range(num)]
    
    if num % 2 != 0:
        for i in range(num):
            answer[i] = total // num + (i - num // 2)
    else:
        for i in range(num):
            answer[i] = total // num + (i - num // 2) + 1
        
    return answer