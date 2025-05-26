def solution(myString, pat):
    answer = 0
    num = len(pat)
    for i in range(len(myString)):
        if pat == myString[i:i+num]:
            answer += 1
    return answer