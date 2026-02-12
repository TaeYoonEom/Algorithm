def solution(a, b):
    answer = 0
    string1 = ''
    string2 = ''
    
    string1 = str(a) + str(b)
    string2 = str(b) + str(a)
    
    if string1 > string2:
        answer = int(string1)
    else:
        answer = int(string2)
    
    return answer