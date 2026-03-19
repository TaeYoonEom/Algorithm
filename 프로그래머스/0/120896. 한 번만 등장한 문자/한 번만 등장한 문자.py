def solution(s):
    answer = ''
    
    for x in s:
        if s.count(x) == 1:
            answer += x
    answer = sorted(answer)
    answer = ''.join(answer)
    return answer