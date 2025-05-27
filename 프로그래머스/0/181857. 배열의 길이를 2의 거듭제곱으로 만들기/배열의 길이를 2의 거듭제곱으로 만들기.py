def solution(arr):
    answer = arr[:]
    length = len(arr)
    
    number = 1
    while number < length:
        number*=2
        
    while len(answer) < number:
        answer.append(0)
            
    return answer