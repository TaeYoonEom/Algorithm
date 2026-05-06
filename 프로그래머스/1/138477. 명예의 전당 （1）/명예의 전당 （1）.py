def solution(k, score):
    answer = []
    result = []
    
    for i in score:
        answer.append(i)
        answer.sort(reverse=True)
        
        if len(answer) > k:
            answer.pop()
        
        result.append(answer[-1])
            
    return result