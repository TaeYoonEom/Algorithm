def solution(arr, k):
    result = []
    count = {}

    for num in arr:
        if num not in count:
            count[num] = True
            result.append(num)
        if len(result) == k:
            break

    while len(result) < k:
        result.append(-1)

    return result
