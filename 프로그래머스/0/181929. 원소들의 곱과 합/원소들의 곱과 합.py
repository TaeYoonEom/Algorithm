def solution(num_list):
    result = 0
    multiply = 1
    numsum = 0
    for i in range(len(num_list)):
        multiply *= num_list[i]
        numsum += num_list[i]
    numsum = numsum**2
    if(multiply < numsum):
        result = 1
    else:
        result = 0
    
    return result