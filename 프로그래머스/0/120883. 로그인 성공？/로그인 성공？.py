def solution(id_pw, db):
    db_dic = dict(db)
    print(db_dic)
    if id_pw[0] in db_dic:
        if id_pw[1] == db_dic[id_pw[0]]:
            return "login"
        else:
            return "wrong pw"
        
    return "fail"