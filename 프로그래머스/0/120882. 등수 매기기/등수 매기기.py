def solution(score):
    
    avg = [(a+b)/2 for a, b in score]
    sorted_avg = sorted(avg, reverse=True)
    return [sorted_avg.index(x)+1 for x in avg]