def solution(x):
    original = x  
    num = 0
    x = str(x)
    
    for i in x:
        num += int(i)
    
    if original % num == 0:
        return True
    else:
        return False
