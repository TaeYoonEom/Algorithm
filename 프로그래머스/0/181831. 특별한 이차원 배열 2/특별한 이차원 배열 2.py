def solution(arr):
    n = len(arr)
    
    for i in range(n):
        for j in range(n):
            if arr[i][j] != arr[j][i]:
                return 0  # 대칭 아님
    return 1  # 모두 대칭
