def solution(arr):
    answer = []
    
    for i in arr: # i = 6 6을 6번 추가해야해
        answer += [i]*i
        
    return answer