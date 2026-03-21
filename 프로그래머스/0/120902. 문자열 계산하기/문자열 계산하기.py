def solution(my_string):
    s = my_string.split()
    
    answer = int(s[0])  # 첫 숫자
    
    for i in range(1, len(s), 2):
        op = s[i]
        num = int(s[i+1])
        
        if op == '+':
            answer += num
        else:
            answer -= num
            
    return answer