def solution(arr, queries):
    answer = []
    
    for a, b in queries:
        num = arr[a] 
        arr[a] = arr[b]
        arr[b] = num 
        
    return arr