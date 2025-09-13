def solution(common):
    # 공차와 공비 계산
    d = common[1] - common[0]
    r = common[1] // common[0] if common[0] != 0 else None

    # 등차수열 판별
    if common[2] - common[1] == d:
        return common[-1] + d
    else:
        return common[-1] * r
