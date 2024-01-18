def solution(numlist, n):
    answer = []
    diff = sorted([i - n for i in numlist])
    dis = sorted([abs(i - n) for i in numlist])
    for i in range(len(numlist) - 1):
        if dis[i] == dis[i+1]:
            dis[i+1] = -dis[i]
    
    for i in range(len(numlist)):
        if dis[i] not in diff:
            dis[i] = -dis[i]
    
    for i in range(len(numlist)):
        answer.append(numlist[numlist.index(dis[i] + n)])
    return answer