def solution(my_string, overwrite_string, s):
    answer = ''
    count = 0
    
        
    count = len(overwrite_string) 
    answer = my_string[:s] + overwrite_string + my_string[s + count:]
    return answer