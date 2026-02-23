def solution(myString, pat):
    answer = 0
    swapString = ""
    for i in range(len(myString)):
        if myString[i] == "A":
            swapString += "B"
        else:
            swapString += "A"
    
    if pat in swapString:
        answer = 1
    else:
        answer = 0
    return answer