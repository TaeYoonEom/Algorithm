def solution(id_pw, db):

    idx = []
    pwx = []
    
    x, y = id_pw
    
    for a,b in db:
        idx.append(a)
        pwx.append(b)
    
    for i in range(len(idx)):
        if x == idx[i] and y == pwx[i]:
            return "login"
        elif x == idx[i] and y != pwx[i]:
            return "wrong pw"
        
    return "fail"
        
            