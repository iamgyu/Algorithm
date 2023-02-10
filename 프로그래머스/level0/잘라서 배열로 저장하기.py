def solution(my_str, n):
    answer = []
    l = len(my_str)
    
    if l % n != 0:
        for i in range(l // n + 1):
            answer.append(my_str[i*n:(i+1)*n])
    else:
        for i in range(l // n):
            answer.append(my_str[i*n:(i+1)*n])
    
    return answer