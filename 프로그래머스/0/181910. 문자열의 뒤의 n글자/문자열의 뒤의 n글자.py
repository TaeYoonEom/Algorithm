def solution(my_string, n):
    answer = ''
    
    lens = len(my_string)
    number = lens - n
    answer = my_string[number:]
    return answer