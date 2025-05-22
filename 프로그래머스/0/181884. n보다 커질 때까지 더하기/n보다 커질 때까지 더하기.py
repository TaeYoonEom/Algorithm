def solution(numbers, n):
    answer = 0
    sums = 0
    for i in numbers:
        sums += i
        if sums > n:
            break
    answer = sums
    return answer