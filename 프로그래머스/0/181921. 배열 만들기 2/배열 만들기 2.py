def solution(l, r):
    answer = []
    
    for i in range(l, r+1):
        s = str(i)
        if all(c in "05" for c in s):
            answer.append(i)
    
    if not answer:
        return [-1]
    
    return answer