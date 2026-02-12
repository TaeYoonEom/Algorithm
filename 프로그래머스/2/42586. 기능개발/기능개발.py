import math

def solution(progresses, speeds):
    answer = []
    number = []
    
    for i in range(len(progresses)):
        number.append(100 - progresses[i])
        
    days = []
    for j in range(len(speeds)):
        days.append(math.ceil(number[j] / speeds[j]))
    
    count = 1
    current = days[0] #days[5,10,1,1,20,1] 
    
    for d in days[1:]:
        if d <= current:
            count += 1
        else:
            answer.append(count)
            current = d
            count = 1
    
    answer.append(count)
    
    return answer