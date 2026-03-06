def solution(n):
    answer = []
    
    for i in range(n):
        rows = []
        for j in range(n):
            if i == j:
                rows.append(1)
            else:
                rows.append(0)
        answer.append(rows)
    return answer