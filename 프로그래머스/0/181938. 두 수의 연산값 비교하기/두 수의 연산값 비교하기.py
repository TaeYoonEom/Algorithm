def solution(a, b):
    answer = 0
    number1 = 0
    number2 = 0
    
    number1 = str(a) + str(b)
    number2 = 2*a*b
    
    if int(number1) > number2:
        answer = int(number1)
    else:
        answer = number2
    return answer