def solution(hp):
    answer = [0, 0, 0] # 4, 1, 0  23 - 20 - 3
    
    answer[0] += hp // 5
    answer[1] += (hp % 5) // 3
    answer[2] += (hp - (5 * answer[0]) - (3 * answer[1]))
    
    return sum(answer)