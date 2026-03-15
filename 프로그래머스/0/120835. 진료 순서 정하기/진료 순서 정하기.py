def solution(emergency):
    
    sorted_arr = sorted(emergency, reverse = True)
    ranks = [sorted_arr.index(x) + 1 for x in emergency]
    return ranks