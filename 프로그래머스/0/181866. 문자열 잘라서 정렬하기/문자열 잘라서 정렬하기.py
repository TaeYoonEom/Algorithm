def solution(myString):
    answer = []
    
    answer = [s for s in myString.split('x') if s]
    answer.sort()
    return answer