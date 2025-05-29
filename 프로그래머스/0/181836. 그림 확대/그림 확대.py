def solution(picture, k):
    result = []
    for row in picture:
        # 각 문자를 k번 반복해서 가로 확대
        stretched_row = ''.join(char * k for char in row)
        
        # 그 줄을 k번 반복해서 세로 확대
        for _ in range(k):
            result.append(stretched_row)
            
    return result
