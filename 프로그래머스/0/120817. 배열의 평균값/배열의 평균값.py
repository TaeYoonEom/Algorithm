def solution(numbers):
    answer = 0
    lens = len(numbers)
    
    for i in range(len(numbers)):
        answer += numbers[i]
    
    answer = answer / lens
    
    return answer