def solution(my_strings, parts):
    answer = ''
    
    for idx in range(len(parts)):
        i, j = parts[idx]
        answer += my_strings[idx][i:j+1]
        
    return answer