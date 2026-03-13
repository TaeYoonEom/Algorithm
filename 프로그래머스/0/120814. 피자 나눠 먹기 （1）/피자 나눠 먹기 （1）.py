def solution(n):
    answer = 0
    ahrt = n // 7
    skajwl = 1
    
    if n <= 7:
        return 1
    elif n > 7:
        if n % 7 == 0:
            answer = ahrt
        elif n % 7 != 0:
            answer = ahrt + skajwl
        
    return answer