def solution(myString):
    result = ''
    
    for ch in myString:
        if ch == 'a':
            result += 'A'
        elif ch != 'A' and ch.isupper():
            result += ch.lower()
        else:
            result += ch
    return result
