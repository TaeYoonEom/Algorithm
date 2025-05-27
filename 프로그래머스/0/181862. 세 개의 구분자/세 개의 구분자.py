def solution(myStr):
    # 1. 모든 구분자를 공통 구분자 하나로 바꾸기
    for ch in 'abc':
        myStr = myStr.replace(ch, '|')
    
    # 2. 나누기
    parts = myStr.split('|')
    
    # 3. 빈 문자열 제거
    result = [s for s in parts if s]
    
    # 4. 결과 없으면 ["EMPTY"]
    return result if result else ["EMPTY"]
