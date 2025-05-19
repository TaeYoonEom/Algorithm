from collections import deque

def solution(l, r):
    result = []
    queue = deque(["5"])  # 0으로 시작하지 않도록 "5"부터 시작

    while queue:
        num_str = queue.popleft()
        num = int(num_str)

        if num > r:
            continue  # r보다 크면 무시

        if l <= num <= r:
            result.append(num)

        # 다음 단계 숫자 생성
        queue.append(num_str + "0")
        queue.append(num_str + "5")

    # 결과가 없으면 -1 반환
    return sorted(result) if result else [-1]
