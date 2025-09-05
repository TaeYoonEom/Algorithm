def solution(num, k):
    answer = 0
    
    new_num = list(str(num))
    for i in range(len(new_num)):
        if new_num[i] == str(k):
            answer = i+1
            break
    if answer == 0:
        answer = -1
    return answer