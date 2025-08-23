def solution(numbers):
    answer = 0
    
    numbers.sort()
    num1 = 0 
    num2 = 0
    
    num1 = numbers[0] * numbers[1]
    num2 = numbers[-2] * numbers[-1]
    if num1 < num2:
        answer = num2
    else:
        answer = num1
    return answer