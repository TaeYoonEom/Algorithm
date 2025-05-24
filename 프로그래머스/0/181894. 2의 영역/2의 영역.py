def solution(arr):
    if 2 not in arr:
        return [-1]  # 2가 하나도 없을 경우

    first = arr.index(2)
    last = len(arr) - 1 - arr[::-1].index(2)
    return arr[first:last + 1]
