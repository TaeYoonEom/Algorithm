def solution(quiz):
    answer = []
    
    for i in quiz:
        parts = i.split('=')
        if eval(parts[0]) == int(parts[1]):
            answer.append("O")
        else:
            answer.append("X")
    return answer