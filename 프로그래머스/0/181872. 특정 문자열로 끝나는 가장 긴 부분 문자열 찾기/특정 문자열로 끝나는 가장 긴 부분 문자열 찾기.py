def solution(myString, pat):
    answer = ''
    
    for i in range(len(myString)):
        if pat == myString[i:i+len(pat)]:
            answer = myString[:i+len(pat)]
    return answer