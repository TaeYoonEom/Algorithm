def solution(my_string):
    answer = 0
    nums = []
    current = ''
    
    for ch in my_string:
        if ch.isdigit():
            current += ch         # 숫자면 이어 붙이기
        else:
            if current:           # 숫자 덩어리 완성되면 저장
                nums.append(int(current))
                current = ""
    if current:  # 마지막에 남은 숫자 처리
        nums.append(int(current))
    
    for i in nums:
        answer += i
    return answer