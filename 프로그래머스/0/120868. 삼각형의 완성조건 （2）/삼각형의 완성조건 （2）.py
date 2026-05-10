def solution(sides):
    answer = 0
    
    small = min(sides)
    big = max(sides)
    
    answer = len(range(big - small + 1, small + big))
    return answer