def solution(order):
    answer = 0
    clap = ['3', '6', '9']
    
    for a in str(order):
        if a in clap:
            answer += 1
            
    return answer
    
    
    
    