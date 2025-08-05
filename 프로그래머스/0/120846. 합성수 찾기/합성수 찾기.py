def solution(n):
    answer = 0

    for i in range(1, n + 1):
        divisor = []
        
        for j in range(1, i + 1):
            if i % j == 0:
                divisor.append(i)
                
        if len(divisor) >= 3:
            answer += 1
            
    return answer