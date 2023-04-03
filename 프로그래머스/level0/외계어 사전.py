def solution(spell, dic):
    for i in dic:
        cmp = 0
        for j in spell:
            if j in i:
                cmp += 1
        if cmp == len(spell):
            return 1
        
    return 2
