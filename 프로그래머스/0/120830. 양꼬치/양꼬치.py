def solution(n, k):
    answer = 0
    
    yang = 12000
    drink = 2000
    service = n // 10
    if service >= 1:
        k = k - service
        
    answer = n * 12000 + drink * k
    return answer