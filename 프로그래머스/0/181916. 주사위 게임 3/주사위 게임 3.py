def solution(a, b, c, d):
    arr = sorted([a,b,c,d])
    
    # 서로 다른 숫자 개수
    unique = len(set(arr))
    
    if unique == 1:
        return 1111 * arr[0]
    
    elif unique == 2:
        if arr.count(arr[0]) == 3 or arr.count(arr[0]) == 1:
            if arr.count(arr[0]) == 3:
                p = arr[0]
                q = arr[3]
            else:
                p = arr[3]
                q = arr[0]
            return (10 * p + q) ** 2
        else:
            p = arr[0]
            q = arr[2]
            return (p+q) * abs(p - q)
            
    elif unique == 3:
        for num in arr:
            if arr.count(num) == 1:
                if 'q' not in locals():
                    q = num
                else:
                    r = num
        return q * r
    else:
        return arr[0]
        
            
    
    
    
    return answer