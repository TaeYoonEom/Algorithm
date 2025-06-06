def solution(num_list):
    answer = []
    left = 0
    right = 0
    
    for i in range(len(num_list)):
        if num_list[i] % 2 == 0:
            left += 1
        else:
            right += 1
    answer += (left, right)
    return answer