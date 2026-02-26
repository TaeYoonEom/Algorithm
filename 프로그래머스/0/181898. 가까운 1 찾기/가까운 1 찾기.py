def solution(arr, idx):
    for i in range(idx, len(arr)):   # idx 포함
        if arr[i] == 1:
            return i
    return -1
        
    ## idx 보다 인덱스가 크면서 값이 1인 가장 작은 인덱스 