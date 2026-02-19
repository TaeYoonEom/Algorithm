def solution(ineq, eq, n, m):
    answer = 0
    
    if ineq == "<":
        if eq == "=":
            answer = n <= m
        elif eq == "!":
            answer = n < m
    elif ineq == ">":
        if eq == "=":
            answer = n >= m
        elif eq == "!":
            answer = n > m
        
    if answer == True:
        return 1
    else:
        return 0