def solution(sides):
    answer = 0
    sums = []
    
    sides.sort()
    
    sums += sides[:2]
    
    if sides[-1] < sum(sums):
        answer = 1
    else:
        answer = 2
        
    return answer