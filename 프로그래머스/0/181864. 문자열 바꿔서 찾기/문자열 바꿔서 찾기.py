def solution(myString, pat):
    answer = 0
    string = ''
    
    for i in myString:
        if i == 'A':
            string += 'B'
        elif i == 'B':
            string += 'A'
        else:
            string += i 
    
    if pat in string:
        answer += 1
    else:
        answer += 0
    return answer