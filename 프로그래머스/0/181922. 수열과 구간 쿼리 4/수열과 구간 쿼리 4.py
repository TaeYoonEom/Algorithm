def solution(arr, queries):
    answer = arr
    
    for s, e, k in queries:
        for i in range(s, e+1, k):
            if i % k == 0:
                answer[i] = arr[i] + 1
                
    return answer