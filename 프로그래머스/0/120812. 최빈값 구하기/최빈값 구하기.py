def solution(array):
    count = [0] * (max(array) + 1)	# 횟수 저장할 리스트 초기화
    
    for i in array:
        count[i] += 1				# array 값을 인덱스로 활용해 count 배열에 저장
    
    m = 0							# 여러 개인지 체크용 변수
    for c in count:
        if c == max(count):			
            m += 1					# 해당 인덱스가 최빈값이면 m + 1
    
    if m > 1:						
        return -1					# 최빈값이 여러 개라면 -1 반환
    else:
        return count.index(max(count))