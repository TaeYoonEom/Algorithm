def solution(array):
    answer = 0
    number = len(array)
    num = (number // 2) 
    array.sort()
    answer = array[num]
    
    return answer
        