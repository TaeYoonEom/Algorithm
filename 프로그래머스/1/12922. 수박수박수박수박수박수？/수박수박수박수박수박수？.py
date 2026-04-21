def solution(n):
    answer = ''
    
    alpha = "수박"
    if n % 2 == 0:
        return (n // 2) * alpha
    else:
        return (n // 2) * alpha + "수"