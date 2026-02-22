def solution(arr, queries):
    answer = []
    
    for s, e, k in queries:
        sub = arr[s:e+1]
        
        candidates = []
        for x in sub:
            if x > k:
                candidates.append(x)
        
        if candidates:
            answer.append(min(candidates))
        else:
            answer.append(-1)
        
    return answer