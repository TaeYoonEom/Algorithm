def solution(n):
    result = ""
    while n > 0:
        # 3으로 나눈 나머지를 문자열 앞에 붙임
        result = str(n % 3) + result
        # 3으로 나눈 몫으로 갱신
        n //= 3
    result = result[::-1]

    return int(result, 3)