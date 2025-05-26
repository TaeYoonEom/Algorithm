def solution(rny_string):
    answer = ''
    
    for ch in rny_string:
        if ch == 'm':
            answer += 'rn'
        else:
            answer += ch
    return answer