def solution(num_list):
    answer = 0
    num1 = 1
    if len(num_list) >= 11:
        answer = sum(num_list)
    elif len(num_list) <= 10:
        for i in num_list:
            num1 *= i
        answer = num1
    return answer