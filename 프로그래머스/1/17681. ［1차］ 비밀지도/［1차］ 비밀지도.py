def solution(n, arr1, arr2):
    answer = []
    
    for i in range(n):
        binary_row = bin(arr1[i] | arr2[i])[2:].zfill(n)
        rows = binary_row.replace('1', '#').replace('0', ' ')
        answer.append(rows)
        
    return answer