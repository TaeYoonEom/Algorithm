def solution(numbers, k):
    idx = 2 * (k - 1)  # 한 번에 2명씩 이동, k번째는 (k-1)번 이동
    return numbers[idx % len(numbers)]
