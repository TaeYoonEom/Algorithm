def solution(a, b, n):
    answer = 0 
    
    while n >= a:
        # 1. 이번에 바꿀 수 있는 콜라 묶음 수 = n // a
        # 2. 새로 받은 콜라 수 = (묶음 수) * b
        new_cola = (n // a) * b
        
        # 3. 남은 빈 병 = (바꾸고 남은 병) + (새로 마셔서 생긴 빈 병)
        remain = n % a
        
        answer += new_cola # 총 마신 콜라 수 누적
        n = new_cola + remain # 이제 내 손에 있는 총 빈 병 업데이트
        
    return answer