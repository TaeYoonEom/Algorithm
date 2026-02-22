def solution(n):
    answer = []
    
    while True:
        answer.append(n)
    
        if n == 1:
            break
        elif n % 2 == 0:
            n = n // 2
        elif n % 2 == 1:
            n = n * 3 + 1
    
    return answer