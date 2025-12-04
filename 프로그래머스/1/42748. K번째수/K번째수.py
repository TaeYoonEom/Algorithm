def solution(array, commands):
    answer = []
    arr = []
    for i, j, z in commands:
        arr = array[i-1:j]
        arr.sort()
        answer.append(arr[z-1])
    return answer