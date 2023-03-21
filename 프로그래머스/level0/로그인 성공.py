def solution(id_pw, db):
    answer = ''
    for i in range(len(db)):
        if id_pw[0] == db[i][0]:
            answer = 'wrong pw'
            break
        else:
            answer = 'fail'
            
    if id_pw in db:
        answer = 'login'
    return answer