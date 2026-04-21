def solution(left, right):
    dictc = {}
    answer = 0
    for i in range(left, right+1):
        count = 0
        for j in range(1, i+1):
            if i % j == 0:
                count += 1
            dictc[i] = count
    for key, value in dictc.items():
        if value % 2 == 0:
            answer += key
        else:
            answer -= key
        
    return answer