def solution(arr):
    
    for i in range(1000):
        if len(arr) <= 2**i:
            arr += [0] * (2**i - len(arr))
            break
    return arr