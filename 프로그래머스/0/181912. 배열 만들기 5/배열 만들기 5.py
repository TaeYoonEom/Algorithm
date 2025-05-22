def solution(intStrs, k, s, l):
    answer = []
    
    for item in intStrs:
        substr = item[s:s+l]
        num = int(substr)
        if num > k:
            answer.append(num)
    return answer