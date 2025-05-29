def solution(arr):
    row_len = len(arr)
    col_len = len(arr[0])
    
    # 1. 행 > 열: 각 행에 0 추가
    if row_len > col_len:
        for row in arr:
            row.extend([0] * (row_len - col_len))
    
    # 2. 열 > 행: 0으로 된 행 추가
    elif col_len > row_len:
        for _ in range(col_len - row_len):
            arr.append([0] * col_len)
    
    return arr
