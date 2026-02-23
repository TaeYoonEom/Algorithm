def solution(arr):
    stk = []
    i = 0
    
    while i < len(arr):
        if not stk:
            stk.append(arr[i])
            i += 1
        elif arr[i] > stk[-1]:
            stk.append(arr[i])
            i += 1
        else:
            stk.pop()
    
    return stk