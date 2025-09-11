def solution(sides):
    answer = 0
    a, b = sides
    big = max(a, b)
    small = min(a, b)
    total = a + b

    # 세 번째 변이 가장 긴 변일 때 (small+1 ~ big)
    for i in range(big - small + 1, big + 1):
        answer += 1

    # 기존 큰 변이 가장 긴 변일 때 (big+1 ~ total-1)
    for i in range(big + 1, total):
        answer += 1

    return answer
