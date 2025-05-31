def solution(array):
    # 각 값의 등장 횟수를 저장할 리스트
    counts = [array.count(i) for i in array]
    
    # 최댓값 등장 횟수와 해당 숫자 구하기
    max_count = max(counts)
    max_values = [array[i] for i in range(len(array)) if counts[i] == max_count]

    # 중복 제거
    max_values = list(set(max_values))
    
    # 최빈값이 하나면 그 값을, 아니면 -1 반환
    return max_values[0] if len(max_values) == 1 else -1
