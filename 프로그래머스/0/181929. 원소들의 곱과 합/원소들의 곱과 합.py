def solution(num_list):
    qwer = 1
    sums = 0
    
    for i in num_list:
        sums += i
        qwer *= i
    
    sums = sums**2
    
    if qwer < sums:
        return 1
    else:
        return 0
        
