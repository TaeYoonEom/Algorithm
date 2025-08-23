def solution(s):
    stack = []
    for token in s.split():   # 문자열을 공백으로 쪼갬
        if token == 'Z':
            if stack:         # 직전 숫자가 있으면 취소
                stack.pop()
        else:
            stack.append(int(token))  # 문자열 → 정수 변환
    return sum(stack)
