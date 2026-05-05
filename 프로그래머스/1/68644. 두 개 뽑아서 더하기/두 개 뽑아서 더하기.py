def solution(numbers):
    
    result_set = set()
    
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            result_set.add(numbers[i] + numbers[j])
            
    return sorted(result_set)