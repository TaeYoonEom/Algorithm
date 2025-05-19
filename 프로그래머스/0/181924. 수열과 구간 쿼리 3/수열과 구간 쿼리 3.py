def solution(arr, queries):
    answer = []
    index = []
    
    for i, j in queries:
        index = arr[i]
        arr[i] = arr[j]
        arr[j] = index
        
    answer = arr
    return answer