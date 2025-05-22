def solution(a, b, c, d):
    from collections import Counter

    nums = [a, b, c, d]
    count = Counter(nums)
    freq = sorted(count.items(), key=lambda x: -x[1])  # 등장 횟수로 정렬

    if len(count) == 1:
        # 조건 1: 네 개 모두 같음
        return 1111 * freq[0][0]
    
    elif len(count) == 2:
        # 조건 2 or 3
        if freq[0][1] == 3:
            # 조건 2: 3개 같고 1개 다름
            p = freq[0][0]
            q = freq[1][0]
            return (10 * p + q) ** 2
        else:
            # 조건 3: 2개 + 2개
            p = freq[0][0]
            q = freq[1][0]
            return (p + q) * abs(p - q)
    
    elif len(count) == 3:
        # 조건 4: 한 쌍만 있고 나머지 다 다름
        pair = [k for k, v in count.items() if v == 2][0]
        others = [k for k, v in count.items() if v == 1]
        return others[0] * others[1]

    else:
        # 조건 5: 전부 다름
        return min(nums)
