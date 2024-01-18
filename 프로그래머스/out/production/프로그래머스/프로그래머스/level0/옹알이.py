def solution(babbling):
    arr = ["aya", "ye", "woo", "ma"]
    answer = 0
    
    for i in babbling:
        for j in arr:
            i = i.replace(j, "@")
        if i.replace("@", "") == "":
            answer += 1
            
    return answer