def solution(quiz):
    answer = []
    
    for q in quiz:
        # "3 - 4 = -1" -> ["3 - 4", "-1"]
        left, right = q.split("=")
        
        # 왼쪽 부분 계산
        if eval(left) == int(right):
            answer.append("O")
        else:
            answer.append("X")
    return answer
