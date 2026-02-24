def solution(n):
    answer = 0
    
    n = str(n)
    answer = sorted(n, reverse=True)
    return int("".join(answer))